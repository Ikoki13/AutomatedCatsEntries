import json

class ConfigFileReader:
    filePath = ''
    fileContent = ''

    def __init__(self, path):
        self.filePath = path

    def readConfigFile(self):
        try:
            with open(self.filePath, 'r') as file:
                self.fileContent = json.load(file)
        except FileNotFoundError:
            print(f"File not found: {self.filePath}")
            return None
        except json.JSONDecodeError:
            print(f"Invalid JSON format in file: {self.filePath}")
            return None

