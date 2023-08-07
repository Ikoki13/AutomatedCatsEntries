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