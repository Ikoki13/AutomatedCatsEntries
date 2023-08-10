from base64 import b64encode

import requests
import json

from Classes.GeneralTimeEntry import GeneralTimeEntry
from ToolApiManager.baseApiManager import BaseApiManager


class TogglApiManager(BaseApiManager):
    def __init__(self, workspaceId, projectId, token, startDate, endDate):
        super().__init__()
        self.workspaceId = int(workspaceId)
        self.projectId = int(projectId)
        self.token = token
        self.startDate = startDate
        self.endDate = endDate

    def readTasksForToday(self):
        print("fetching for {}".format(self.startDate))
        apiToken = self.token + ":api_token"

        # TODO filter current running taks (duration is negative) (done ;))
        response = requests.get(
            "https://api.track.toggl.com/api/v9/me/time_entries?start_date={}&end_date={}".format(
                self.startDate, self.endDate
            ),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Basic %s"
                % b64encode(apiToken.encode("utf-8")).decode("ascii")

            },
        )
        print("fetching successful")
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
            if e["duration"] >= 0:
                result.append(
                    GeneralTimeEntry(e["description"], e["duration"], e["tags"])
                )
        return result
