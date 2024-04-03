from Classes.CATsCell import CATsCell


class CATsRow:
    def __init__(self, timeEntries):
        self.listOfTimeEntries = []

        from main import jsonData
        useSingleBlockForAllEntries = jsonData['useSingleBlockForAllEntries']

        # Anwenden der Konfiguration
        if useSingleBlockForAllEntries:
            # Füge alle Einträge in einem einzigen Block hinzu
            self.listOfTimeEntries.extend(self.addEntriesToCATsCells(timeEntries))
        else:
            # Trenne Termine und Nicht-Termine in verschiedene Blöcke
            terminEntries = [e for e in timeEntries if 'termin' in [tag.lower() for tag in e.tags]]
            nonTerminEntries = [e for e in timeEntries if 'termin' not in [tag.lower() for tag in e.tags]]

            self.listOfTimeEntries.extend(self.addEntriesToCATsCells(terminEntries))
            self.listOfTimeEntries.extend(self.addEntriesToCATsCells(nonTerminEntries))

        # Funktion zum Hinzufügen von Einträgen in CATsCell unter Berücksichtigung der Zeichenbegrenzung
    def addEntriesToCATsCells(self, entries):
        cells = []
        currentCell = CATsCell()
        for entry in entries:
            if not currentCell.addTimeEntry(entry):
                cells.append(currentCell)
                currentCell = CATsCell()
                currentCell.addTimeEntry(entry)  # Wir nehmen an, dass ein einzelner Eintrag nicht die Maximalgröße überschreitet
        cells.append(currentCell)  # Füge die letzte CATsCell hinzu

        if not cells[-1].cellText:
                cells.pop()
        return cells

    def __str__(self):
        result = ''
        for entry in self.listOfTimeEntries:
            result += str(entry) + "\n"
        return result
