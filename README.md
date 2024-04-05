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

## Feature-Toggle für die Behandlung von Zeiteinträgen - 02.04.2024

In unserer Anwendung haben wir einen Feature-Toggle implementiert, der es ermöglicht, das Verhalten bei der Verarbeitung und Gruppierung von Zeiteinträgen dynamisch zu steuern. Dieser Toggle wird über unsere Konfigurationsdatei (`config.json`) gesteuert und bietet Flexibilität in der Darstellung und Handhabung der Zeiteinträge.

### Konfiguration
Der Toggle wird durch den Schlüssel `useSingleBlockForAllEntries` in der `config.json`-Datei gesteuert. Er akzeptiert einen booleschen Wert (`true` oder `false`):

- `true`: Alle Zeiteinträge werden in einem einzigen Block zusammengefasst, ohne Unterscheidung zwischen verschiedenen Typen von Einträgen.

- `false`: Zeiteinträge werden basierend auf ihren Tags in unterschiedliche Blöcke gruppiert. Einträge mit dem Tag `termin` werden separat von anderen Einträgen behandelt, um eine klare Unterscheidung und Strukturierung zu gewährleisten.

### Anwendung des Toggles
Der Toggle wird beim Initialisieren der `CATsRow`-Klasse berücksichtigt. Basierend auf dem Wert von useSingleBlockForAllEntries wählt die Klasse die entsprechende Logik zur Gruppierung der Zeiteinträge:

1. **Einzelblock-Modus (`useSingleBlockForAllEntries` ist `true`):** In diesem Modus werden alle Zeiteinträge, unabhängig von ihren Tags, in einem einzigen Block zusammengefasst. Dies vereinfacht die Darstellung, indem es die Unterscheidung zwischen verschiedenen Arten von Aktivitäten (wie Termine, Entwicklung, Analyse etc.) ignoriert.
2. **Getrennte Blöcke (`useSingleBlockForAllEntries` ist `false`):** In diesem Modus werden Zeiteinträge sorgfältig nach ihren Tags gruppiert. Einträge mit dem Tag `termin` werden von anderen Aktivitätstypen getrennt, um eine klare visuelle und organisatorische Trennung in der Ausgabe zu gewährleisten.

### Beispiel `config.json`
````
{
  "tool": "toggl",
  "token": "564280678bc42ea1203e73ce107cb244",
  "workspaceId": "7596813",
  "projectId": "195060378",
  "browser": "chrome",
  "leistungsart": "BXACIB",
  "useSingleBlockForAllEntries": false
}
````
Durch Anpassen des Werts von `useSingleBlockForAllEntries` in der Konfigurationsdatei können Entwickler und Nutzer das Verhalten der Anwendung leicht ändern, um ihren spezifischen Anforderungen gerecht zu werden.