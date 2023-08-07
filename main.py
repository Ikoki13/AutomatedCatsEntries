import pickle

from Classes.CATsRow import CATsRow
from ToolApiManager.togglApiManager import TogglApiManager
from configFileReader import ConfigFileReader

fileConfig = ConfigFileReader('config.json')
fileConfig.readConfigFile()
jsonData = fileConfig.fileContent

if(jsonData['tool'] == "toggl"):
    apiManager = TogglApiManager(jsonData['workspaceId'], jsonData['projectId'], jsonData['token'])
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
with open(file_name, 'w', encoding="utf-8") as file:
    file.write(catsRow.__str__())
    #pickle.dump(catsRow, file)