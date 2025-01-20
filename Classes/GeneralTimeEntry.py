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
        description = self.description
        duration = self.formatSecondsToQuarterlyHours(self.duration)
        lowerCaseTags = list(map(lambda t:t.lower(), self.tags))
        milestone = self.getFirstTagStartingWithM(lowerCaseTags).upper()

        # find description
        if 'termin' in lowerCaseTags:
            description = "Teilnahme Termin '" + self.description + "'"
        elif 'vorbereitung' in lowerCaseTags:
            description = "Vorbereitung '" + self.description + "'"
        elif 'nachbereitung' in lowerCaseTags:
            description = "Nachbereitung '" + self.description + "'"
        elif 'protokoll' in lowerCaseTags:
            description = "Erstellung Protokoll für '" + self.description + "'"
        elif 'entwicklung' in lowerCaseTags:
            description = "Entwicklung " + self.description
        else:
            description = self.description

        result = duration + "h " + milestone + description

        return result

    def formatSecondsToQuarterlyHours(self, seconds):
        quarter_hours = round(seconds / 900)
        if quarter_hours == 0: 
            quarter_hours = 1
        return str(quarter_hours / 4)

    def getFirstTagStartingWithM(self, tags):
    # Find the first tag that starts with 'm'
        for tag in tags:
            if tag.startswith('m'):
                return tag + " "
        return ""  # Return None if no tag starts with 'm'

