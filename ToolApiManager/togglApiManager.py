from base64 import b64encode

import requests

from Classes.GeneralTimeEntry import GeneralTimeEntry
from ToolApiManager.baseApiManager import BaseApiManager


class TogglApiManager(BaseApiManager):
    def __init__(self, workspaceId, projectId, token):
        super().__init__()
        self.workspaceId = int(workspaceId)
        self.projectId = int(projectId)
        self.token = token

    def readTasksForToday(self):
        print("fetching tasks from today")
        # TODO add today as parameter and not make it hard coded
        # TODO make token variable from config
        # TODO filter current running taks (duration is negative)
        response = requests.get("https://api.track.toggl.com/api/v9/me/time_entries?start_date={}&end_date={}".format(
            "2023-08-07T00:00:00.00Z", "2023-08-07T23:59:59.99Z"),
                                headers={'Authorization': 'Basic %s' % b64encode(
                                    b"bb1d364bc0b2eacb2b2455e7d67202e6:api_token").decode("ascii")})
        print("fetching successful")
        filteredTaskList = filter(lambda task: task['project_id'] == self.projectId, response.json())
        return filteredTaskList

    def mapToGeneralTimeEntries(self, timeEntryList):
        result = list()

        for e in timeEntryList:
            result.append(GeneralTimeEntry(e['description'], e['duration'],e['tags']))
        return result