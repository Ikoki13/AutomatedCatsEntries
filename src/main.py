import sys
from calendar import monthrange
from datetime import datetime, date, timezone

from src.Classes.CATsRow import CATsRow
from ToolApiManager.togglApiManager import TogglApiManager
from configFileReader import ConfigFileReader
from src.Helpers.dateHelper import get_formatted_date, calculate_date_difference

# Check for command-line arguments and determine the date range
args = sys.argv[1:]
start_dt, end_dt = None, None

if "-t" in args or "--today" in args:
    start_dt = datetime.now(tzinfo=timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    end_dt = datetime.now(tzinfo=timezone.utc).replace(hour=23, minute=59, second=59, microsecond=999999)

elif "-m" in args or "--month" in args:
    today = date.today()
    # the first value (the weekday) is assigned to the underscore (_).
    # This is a common Python convention used to indicate a value that you don't need and will discard.
    _, last_day = monthrange(today.year, today.month)
    start_dt = datetime(today.year, today.month, 1, tzinfo=timezone.utc)
    end_dt = datetime(today.year, today.month, last_day, 23, 59, 59, 999999, tzinfo=timezone.utc)

else:
    # Get dates from user input if no specific argument is provided
    start_dt = get_formatted_date("Please input start date [dd.mm.YYYY] or press enter for today: ")
    end_dt = get_formatted_date("Please input end date [dd.mm.YYYY] or press enter for today: ")
    # Ensure end_dt is after start_dt
    if start_dt > end_dt:
        start_dt, end_dt = end_dt, start_dt

    end_dt = end_dt.replace(hour=23, minute=59, second=59)

# Centralized calculation and logic
if start_dt and end_dt:
    days_diff = calculate_date_difference(start_dt, end_dt)
    print(f"The number of days between the dates is: {days_diff}")

    addDayToExport = days_diff > 1
else:
    print("❌ Could not determine a valid date range.")

## read JSON Config file
fileConfig = ConfigFileReader("../config.json")
fileConfig.readConfigFile()
jsonData = fileConfig.fileContent

if jsonData["tool"] == "toggl":
    apiManager = TogglApiManager(
        jsonData["workspaceId"],
        jsonData["projectId"],
        jsonData["token"],
        start_dt,
        end_dt
    )
else:
    print("Given tool in config not supported")

print("reading tasks for today")
filteredTasks = list(apiManager.readTasksForDates())
print("tasks successfully read - continue mapping")
generalTimeEntries = apiManager.mapToGeneralTimeEntries(filteredTasks)
print("items successfully mapped")

catsRow = CATsRow(generalTimeEntries)
print("im finished")

print("write data to CATs")

print("write data to myTE")

# TODO adapt data export according to single or multiple day export
file_name = "../cats_entries.txt"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(catsRow.__str__())
# pickle.dump(catsRow, file)
