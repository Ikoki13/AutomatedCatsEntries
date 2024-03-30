from Classes.CATsCell import CATsCell

class CATsRow:
    def __init__(self, timeEntries):
        self.listOfTimeEntries = []

        # Zwei Listen für unterschiedliche Eintragstypen: Termine und Nicht-Termine
        terminEntries = [e for e in timeEntries if 'termin' in [tag.lower() for tag in e.tags]]
        nonTerminEntries = [e for e in timeEntries if 'termin' not in [tag.lower() for tag in e.tags]]

        # Funktion zum Hinzufügen von Einträgen in CATsCell unter Berücksichtigung der Zeichenbegrenzung
        def addEntriesToCATsCells(entries):
            cells = []
            currentCell = CATsCell()
            for entry in entries:
                if not currentCell.addTimeEntry(entry):
                    cells.append(currentCell)
                    currentCell = CATsCell()
                    currentCell.addTimeEntry(
                        entry)  # Wir nehmen an, dass ein einzelner Eintrag nicht die Maximalgröße überschreitet
            cells.append(currentCell)  # Füge die letzte CATsCell hinzu
            return cells

        # Termineinträge und Nicht-Termineinträge in getrennten Blöcken hinzufügen
        self.listOfTimeEntries.extend(addEntriesToCATsCells(terminEntries))
        self.listOfTimeEntries.extend(addEntriesToCATsCells(nonTerminEntries))

    def __str__(self):
        result = ''
        for entry in self.listOfTimeEntries:
            result += str(entry) + "\n"
        return result
