# AutomatedCatsEntries

## Prerequisites

- Install python3
- Install necessary python3 modules

## Setup

To setup the tool, change the config.json file in the main repository:
```
{
  "tool": "toggl", // currently no other supported
  "token": "your self created api token in the tool of your choice",
  "workspaceId": "your workspace id",
  "projectId": "your project id",
  "browser": "chrome",
  "leistungsart": "your charge code"
}
```


## Ausgabeformate

| Format        | Tag           | Ausgabe                                 |
|---------------|---------------|-----------------------------------------|
| Termin        | termin        | "[X]h Teilnahme Termin [Terminname]"    |
| Vorbereitung  | vorbereitung  | "Vorbeitung [Content]"                  |
| Nachbereitung | nachbereitung | "Nachbereitung [Content]"               |
| Protokoll     | protokoll     | "Erstellung Protokoll für [Terminname]" |
| Entwicklung   | entwicklung   | "Entwicklung [Content]"                 |
| Analyse       | analyse       | "Analye [Content]"                      |


## Aktualisierte Funktionalität zur Gruppierung von Zeiteinträgen - 30.03.2024

Diese Aktualisierung der CATsRow-Klasse ermöglicht es, Zeiteinträge effizient in Blöcken zu organisieren, wobei Termineinträge gesondert behandelt werden. Termineinträge können zusammen in einem Block erscheinen, solange die maximale Zeichenanzahl des Blocks nicht überschritten wird. Nicht-Termin-Einträge werden ebenfalls in Blöcken gruppiert, dürfen aber nicht mit Termin-Einträgen in einem Block gemischt werden. Dies sorgt für eine klar strukturierte und übersichtliche Ausgabe in der generierten TXT-Datei.

### Funktionsweise

Die CATsRow-Klasse trennt Termineinträge von anderen Eintragstypen und fügt sie in CATsCell-Instanzen ein, wobei die maximale Zeichenbegrenzung jeder Zelle berücksichtigt wird. Hierbei werden zwei Schritte durchgeführt:

Trennung der Einträge: Zeiteinträge werden basierend auf ihren Tags in Termineinträge und Nicht-Termin-Einträge unterteilt.
Blockbildung: Termineinträge werden zuerst in Blöcke eingefügt, gefolgt von Nicht-Termin-Einträgen. Jeder Block versucht, so viele Einträge wie möglich aufzunehmen, ohne die maximale Zeichenbegrenzung zu überschreiten.
Implementierung

```
from .CATsCell import CATsCell

class CATsRow:
    def __init__(self, timeEntries):
        self.listOfTimeEntries = []
        # Trennung der Einträge in Termine und Nicht-Termine
        terminEntries = [e for e in timeEntries if 'termin' in [tag.lower() for tag in e.tags]]
        nonTerminEntries = [e for e in timeEntries if 'termin' not in [tag.lower() for tag in e.tags]]

        # Hinzufügen der Einträge zu CATsCells
        self.listOfTimeEntries.extend(self.addEntriesToCATsCells(terminEntries))
        self.listOfTimeEntries.extend(self.addEntriesToCATsCells(nonTerminEntries))

    def addEntriesToCATsCells(self, entries):
        cells = []
        currentCell = CATsCell()
        for entry in entries:
            if not currentCell.addTimeEntry(entry):
                cells.append(currentCell)
                currentCell = CATsCell()
                currentCell.addTimeEntry(entry)
        if currentCell.cellText:  # Vermeide das Hinzufügen leerer Zellen
            cells.append(currentCell)
        return cells

    def __str__(self):
        result = ''
        for entry in self.listOfTimeEntries:
            result += str(entry) + "\n"
        return result
```
Diese Implementierung stellt sicher, dass Termineinträge nicht mit anderen Eintragsarten gemischt werden und somit eine klare Unterscheidung in der Ausgabe ermöglicht wird.