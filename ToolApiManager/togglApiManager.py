import datetime
from base64 import b64encode

import requests

from Classes.GeneralTimeEntry import GeneralTimeEntry
from ToolApiManager.baseApiManager import BaseApiManager

class TogglApiManager(BaseApiManager):
    def __init__(self, workspaceId, projectId, token):
        super().__init__()
        self.workspaceId = int(workspaceId)
        self.projectId = int(projectId)
        self.token = token + ":api_token"

    def readTasksForToday(self):
        print("fetching tasks from today")
        startDatetime = str(datetime.date.today()) + "T00:00:00.00Z"
        endDatetime = str(datetime.date.today()) + "T23:59:59.99Z"
        # TODO make token variable from config
        response = requests.get("https://api.track.toggl.com/api/v9/me/time_entries?start_date={}&end_date={}".format(startDatetime, endDatetime),
                                headers={'Authorization': 'Basic %s' % b64encode(
                                    self.token.encode()).decode("ascii")})
        print("fetching successful")
        # TODO filter current running taks (duration is negative)
        filteredTaskList = filter(lambda task: task['project_id'] == self.projectId, response.json())
        mergedTasks = self.mergeDuplicatedTasks(filteredTaskList)
        return mergedTasks
    
    def mergeDuplicatedTasks(self, tasks):
        merged_tasks = {}
        for task in tasks:
            key = (task['description'], tuple(task['tags']))
            if key in merged_tasks: 
                merged_tasks[key]['duration'] += task['duration']
                    
            else:
                merged_tasks[key] = task

        merged_list = list(merged_tasks.values())
        return merged_list

    def mapToGeneralTimeEntries(self, timeEntryList):
        result = list()

        for e in timeEntryList:
            result.append(GeneralTimeEntry(e['description'], e['duration'], e['tags']))
        return result