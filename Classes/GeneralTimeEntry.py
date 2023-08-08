class GeneralTimeEntry:
    duration = 0
    tags = []
    description = ''
    def __init__(self, description, duration, tags):
        self.description = description
        self.duration = duration
        self.tags = tags

    def __str__(self):
        print("Description: " + self.description + ", Duration: " + str(self.duration) + ", Tags: " + str(self.tags))

    def getCatFormat(self):
        result = self.description

        # TODO Tag matching case insensitive machen
        # TODO Stunden auf 2 Kommastellen und 15 Minuten Blöcke formattieren
        if 'Termin' in self.tags:
            result = str(float(self.duration/3600)) + "h Teilnahme Termin '" + result + "'"
        elif 'Vorbereitung' in self.tags:
            result = "Vorbereitung '" + result + "'"
        elif 'Nachbereitung' in self.tags:
            result = "Nachbereitung '" + result + "'"
        elif 'Protokoll' in self.tags:
            result = "Erstellung Protokoll für '" + result + "'"
        elif 'Entwicklung' in self.tags:
            result = "Entwicklung von " + result

        return result




