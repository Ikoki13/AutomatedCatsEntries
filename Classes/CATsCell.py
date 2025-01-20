from Classes import GeneralTimeEntry
import logging

class CATsCell:
    maximumNumberOfCharacters = 220
    cellText = ''
    duration = 0.0
    def __init__(self):
        self.cellText = ''
        self.duration = 0.0

    def __str__(self):
        return "Duration:\n" + str(round(self.duration * 4) / 4) + "\nText:\n" + self.cellText

    def addTimeEntry(self, timeEntry):
        result = False
        catsEntry = timeEntry.getCatFormat()

        if len(catsEntry) > self.maximumNumberOfCharacters:
            logging.warning(f"Eintrag zu lang: {catsEntry[:self.maximumNumberOfCharacters]} (Länge: {len(catsEntry)} Zeichen). Eintrag wird nicht hinzugefügt.")
        elif len(self.cellText) + len(catsEntry) <= self.maximumNumberOfCharacters:
            self.cellText = self.cellText + catsEntry + "\n"
            self.duration = self.duration + float(timeEntry.duration/3600)
            result = True
        else:
            logging.info(f"Nicht genug Platz für den gesamten Eintrag.")
        return result

# Testing der Zeichenbegrenzung mit folgendem Text:
#
#Every morning, we are given the chance to create our own story. Today, embrace the possibilities, face challenges with courage, and find joy in the smallest moments. Your journey is unique; make it memorable and impactful.
#
# 222 Zeichen - Danke ChatGPT-4