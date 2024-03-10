import json
import os
import pyperclip as pc
from cryptography.fernet import Fernet

class GeneralUtils():
    def __init__(self):
        self.filepath = "saved_data.json"
        
    def saveToJson(self, data):
        if not self.checkFileExists():
            self.createFile()
        
        key_and_pwBytes = self.hashPassword(data["password"].encode())
        data["password"] = key_and_pwBytes[0]
        data["key"] = key_and_pwBytes[1].decode('utf-8')
        
        with open(self.filepath, "r+") as file:
           if os.path.getsize(self.filepath) > 0:
               saved_data = json.load(file)
               saved_data.append(data)
               file.seek(0)
               json.dump(saved_data, file)
               file.truncate()
           else:
                json.dump([data], file)
                
                
    def openJsonFile(self):
        with open(self.filepath, "r") as file:
            data = json.load(file)
            return data
        
    def checkFileExists(self):
        if os.path.exists(self.filepath):
            return True
        else: 
            return False
                
    def createFile(self):
        with open(self.filepath, "w") as file:
            pass
    
    def find_and_copy(self, url):
        with open(self.filepath, "r") as file:
            datas = json.load(file)
            for data in datas:
                for key, value in data.items():
                    if url in value:
                        decoded_pw = self.decryptPassword(data["password"], data["key"])
                        pc.copy(decoded_pw)
                        print("Password has been copied to clipboard")
                    
        
    def hashPassword(self, pw):
        key = Fernet.generate_key()
        f = Fernet(key)
        return [f.encrypt(pw).decode('utf-8'), key]
    
    def decryptPassword(self, pw, key):
        f = Fernet(key.encode('utf-8'))
        return f.decrypt(pw).decode('utf-8')
            
        