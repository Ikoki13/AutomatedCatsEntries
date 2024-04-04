class BaseApiManager:
    def readTasksForToday(self):
        raise NotImplementedError("Subclass must implement this method")

    def mapToGeneralTimeEntries(self, timeEntries):
        raise NotImplementedError("Subclass must implement this method")

