import pickle
import sys

from datetime import datetime, date

from Classes.CATsRow import CATsRow
from ToolApiManager.togglApiManager import TogglApiManager
from configFileReader import ConfigFileReader

fileConfig = ConfigFileReader("config.json")
fileConfig.readConfigFile()
jsonData = fileConfig.fileContent

# enable command line parameter "-t" (short) and "--today" (long) for todays date
if len(sys.argv) == 2 and sys.argv[1] in  ("-t", "--today"):
    startDate = date.today().strftime("%Y-%m-%dT00:00:00Z")
    endDate = date.today().strftime("%Y-%m-%dT23:59:59Z")
else:
    inputDate = input("Please input date [dd.mm.YYYY] or no date for today: ")
    # giving the date format
    date_format = "%d.%m.%Y"
    try:
        print(
            "Using date: "
            + datetime.strptime(inputDate, date_format).strftime("%Y-%m-%dT00:00:00Z")
        )
        startDate = datetime.strptime(inputDate, date_format).strftime("%Y-%m-%dT00:00:00Z")
        endDate = datetime.strptime(inputDate, date_format).strftime("%Y-%m-%dT23:59:59Z")
    except:
        print("Wrong date format or no date provided.")
        print("Using today: " + date.today().strftime("%Y-%m-%dT00:00:00Z"))
        startDate = date.today().strftime("%Y-%m-%dT00:00:00Z")
        endDate = date.today().strftime("%Y-%m-%dT23:59:59Z")

if jsonData["tool"] == "toggl":
    apiManager = TogglApiManager(
        jsonData["workspaceId"],
        jsonData["projectId"],
        jsonData["token"],
        startDate,
        endDate,
    )
else:
    print("Given tool in config not supported")

print("reading tasks for today")
filteredTasksFromToday = list(apiManager.readTasksForToday())
print("tasks successfully read - continue mapping")
generalTimeEntries = apiManager.mapToGeneralTimeEntries(filteredTasksFromToday)
print("items successfully mapped")

catsRow = CATsRow(generalTimeEntries)
print("im finished")

print("write data to CATs")

print("write data to myTE")

file_name = "cats_entries.txt"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(catsRow.__str__())
# pickle.dump(catsRow, file)
