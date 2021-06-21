import json

#Open a json file when format is [{a,b}, {d,e}]. ie. records are in a python dictionary format already
class MyFile:
    def __init__(self,file_path):
        self.path=file_path

class JsonFileReader:
    def read_file(self,file_path):
         with open(file_path,'r') as f:
            data = json.load(f)
            return data        
        
file= MyFile("C:/Users/MMZ/code/py_data_etl/jsondict_format.json") 
file_reader = JsonFileReader()
records = file_reader.read_file(file.path)
print(records)
