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
        lowerCaseTags = list(map(lambda t:t.lower(), self.tags))
        
        if 'termin' in lowerCaseTags:
            result = self.formatSecondsToQuarterlyHours(self.duration) + "h Teilnahme Termin '" + result + "'"
        elif 'vorbereitung' in lowerCaseTags:
            result = "Vorbereitung '" + result + "'"
        elif 'nachbereitung' in lowerCaseTags:
            result = "Nachbereitung '" + result + "'"
        elif 'protokoll' in lowerCaseTags:
            result = "Erstellung Protokoll für '" + result + "'"
        elif 'entwicklung' in lowerCaseTags:
            result = "Entwicklung " + result

        return result

    def formatSecondsToQuarterlyHours(self, seconds):
        quarter_hours = round(seconds / 900)
        if quarter_hours == 0: 
            quarter_hours = 1
        return str(quarter_hours / 4)



