import requests
import json

class ffinit:

    def __init__(self, path) -> None:
        self.loadInitFile(path)
        self.getSettings()
        self.setHeaders()
        self.checkAuthentication()
        self.importData()

    def loadInitFile(self, path):
        jsonFile = open(path)
        self.data = json.load(jsonFile)
        jsonFile.close()
    
    def getSettings(self):
        self.host = self.data['settings']['host']
        self.token = self.data['settings']['token']

    def setHeaders(self):
        self.headers = {
            'User-Agent': 'ffinit',
            'accept': 'application/vnd.api+json',
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json'
        }
    
    def checkAuthentication(self):
        url = self.host + "/api/v1/about"
        r = requests.get(url, headers=self.headers)
        if not r.status_code == requests.codes.ok:
            print(r.raise_for_status())
            r.close()
            exit()
        print("Authorization successfull")

    def importData(self):
        for key, value in self.data.items():
            if key == "settings":
                continue
            url = self.host + value['url']
            for innerkey, innervalue in value.items():
                if innerkey == "url":
                    continue
                for item in innervalue:
                    r = requests.post(url, headers=self.headers, json=item)

init = ffinit("/scripts/init.json")