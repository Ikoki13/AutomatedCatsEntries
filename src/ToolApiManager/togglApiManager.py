import calendar
from base64 import b64encode
from datetime import datetime

import requests

from src.Classes.GeneralTimeEntry import GeneralTimeEntry
from src.ToolApiManager.baseApiManager import BaseApiManager


class TogglApiManager(BaseApiManager):
    def __init__(self, workspaceId, projectId, token, startDate, endDate):
        super().__init__()
        self.workspaceId = int(workspaceId)
        self.projectId = int(projectId)
        self.token = token
        self.startDate = startDate
        self.endDate = endDate

    def readTasksForDates(self):
        print("fetching data from {} to {}".format(self.startDate, self.endDate))

        credentials = f"{self.token}:api_token"
        encoded_credentials = b64encode(credentials.encode("utf-8")).decode("ascii")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {encoded_credentials}"
        }
        params = {
            "start_date": self.startDate.isoformat(),
            "end_date": self.endDate.isoformat(),
        }
        response = requests.get(
            "https://api.track.toggl.com/api/v9/me/time_entries",
            headers=headers,
            params=params
        )

        print("fetching successful")
        if(response.status_code == 200):
            filteredTaskList = filter(lambda task: task['project_id'] == self.projectId, response.json())
            mergedTasks = self.mergeDuplicatedTasks(filteredTaskList)

        return mergedTasks

    def readTasksForMonth(self, month, year):
        # Calculate first and last day of the month
        first_day = datetime(year, month, 1)
        last_day = datetime(year, month, calendar.monthrange(year, month)[1])

        # Format dates as ISO 8601
        start_date = first_day.strftime("%Y-%m-%dT00:00:00+00:00")
        end_date = last_day.strftime("%Y-%m-%dT23:59:59+00:00")

        print(f"Fetching for month: {month}/{year} ({start_date} to {end_date})")
        apiToken = self.token + ":api_token"

        response = requests.get(
            f"https://api.track.toggl.com/api/v9/me/time_entries?start_date={start_date}&end_date={end_date}",
            headers={
                "Content-Type": "application/json",
                "Authorization": "Basic %s" % b64encode(apiToken.encode("utf-8")).decode("ascii")
            },
        )
        print("Fetching successful")
        filteredTaskList = filter(lambda task: task['project_id'] == self.projectId, response.json())
        mergedTasks = self.mergeDuplicatedTasks(filteredTaskList)
        return mergedTasks

    def mergeDuplicatedTasks(self, tasks):
        merged_tasks = {}
        for task in tasks:
            key = (datetime.fromisoformat(task['start']).date(), task['description'], tuple(task['tags']))
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
                    GeneralTimeEntry(e["description"], e["duration"], e["tags"], e["start"])
                )
        return result
