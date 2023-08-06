from configFileReader import ConfigFileReader
from base64 import b64encode
import requests

fileConfig = ConfigFileReader('config.json')
fileConfig.readConfigFile()
jsonData = fileConfig.fileContent

if fileConfig.fileContent is not None:
    api_token = "{}:api_token".format(jsonData['token'])
    taskEndpoint = jsonData['baseEndpoint'] + jsonData['taskEndpoint'].format(jsonData['workspaceId'],
                                                                              jsonData['projectId'])
    print("endpoint to call: " + taskEndpoint)
    print("token to use: " + api_token)

response = requests.get(taskEndpoint,
                    headers={'content-type': 'application/json',
                             'Authorization': 'Basic %s' % b64encode(b"bb1d364bc0b2eacb2b2455e7d67202e6:api_token").decode("ascii")})
print(response)
