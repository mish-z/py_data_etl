import json
#Turn json records into tabulated data frame
#the file format here is multiple json records without being in an array format, 
#so convert file into the correct format first for json.load to decode.

file_path="C:/Users/~~/fossil_species.json"

#convert file into a list of json records
with open(file_path) as f:
    data = json.loads("[" + 
        f.read().replace("}\n{", "},\n{") + 
    "]")

#each item in list is a dictionary
#count the number of records
record_count=len(data)
print("Total number of records: " + str(record_count))

def tabulate_json_records(records):
#tabulate the dictionaries inside a list of dictionaries
    print("id:" + "\t" + "type:\t\t" + "species:\t\t" + "\n")
    for dic in records:
        print(dic["id"] + "\t" + dic["type"] + "\t" + dic["species"] + "\n")
    
    #for val in dic.values():
        #print(val)
 
tabulate_json_records(data)