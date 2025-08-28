class BaseApiManager:
    def readTasksForDates(self):
        raise NotImplementedError("Subclass must implement this method")

    def mapToGeneralTimeEntries(self, timeEntries):
        raise NotImplementedError("Subclass must implement this method")

