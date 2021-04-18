#coding=utf-8
import os
import sys
import configparser
base_path=os.getcwd()
sys.path.append(base_path)
# config = configparser.ConfigParser()
# config.read(base_path+'/config/server.ini',encoding='utf-8')

# a = config.get("server", "host")
#print(a)
class HandleIni:
    
    def load_ini(self):
        config = configparser.ConfigParser()
        config.read(base_path+'/config/server.ini',encoding='utf-8')
        return config
    def get_value(self,key,section=None):
        config=self.load_ini()
        if section == None:
            section= "server"
        try:

           data = config.get(section,key)
        except:
            print("没有这个key")
            data=None
        return data
handleIni=HandleIni()
if __name__ == "__main__":
    handleIni=HandleIni()
    print(handleIni.get_value('host'))


    
