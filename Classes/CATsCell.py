from Classes import GeneralTimeEntry

class CATsCell:
    maximumNumberOfCharacters = 220
    cellText = ''
    duration = 0.0
    def __init__(self):
        self.cellText = ''
        self.duration = 0.0

    def __str__(self):
        return "Duration:\n" + str(self.duration) + "\nText:\n" + self.cellText

    def addTimeEntry(self, timeEntry):
        result = False
        catsEntry = timeEntry.getCatFormat()

        # TODO wenn ein einziger Eintrag zu lange ist, disen rot raus loggen bzw. Benutzer
        if len(self.cellText) + len(catsEntry) < self.maximumNumberOfCharacters:
            self.cellText = self.cellText + catsEntry + "\n"
            self.duration = self.duration + float(timeEntry.duration/3600)
            result = True

        return result