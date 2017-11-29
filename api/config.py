import yaml
import json

class Config:

    def saveconfig(self,data, configfile="signal.conf"):
        with open(configfile, 'w') as config:
            json.dump(data,config)
            return True


    def loadconfig(self,data, configfile="signal.conf"):
        with open(configfile, 'r') as config:
            return json.loads(config)

    def appendconfig(self,message,configfile="signal.conf"):
        try:
            with open(configfile, 'a') as config:
                return json.dump(message,config)
        except FileNotFoundError as e:
            return self.saveconfig(message)
