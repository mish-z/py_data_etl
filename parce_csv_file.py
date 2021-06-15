# Converts lines in a csv file into sql statements


file_path="C:/Users/MMZ/code/sample_python/csv-list.csv"
output_path="C:/Users/MMZ/code/sample_python/sql_stats.sql"

output_file = open(output_path, "w")
with open(file_path,"r") as mfile:
    for row in mfile:
        # Parse each line in the CSV file as a row
        #Only format if row is not a new line
        if(row != "\n"):
            #strings are immutable, lower() returns a new string so print(row) returns unchanged string
            new_string=row.lower()
            #Split the items in the row and strip leading&trailing whitespace
            details_list=new_string.split(",")
                
            food=details_list[0].strip()
            weight=details_list[1].strip()
            calories=details_list[2].strip()
            
            # sql statement 
            # %s replaced with values from a tuple after % operator
            sql_insert = "insert into food (name,food_weight, food_calories) values ('%s','%s','%s')" % (food,weight,calories)
            #write insert sql statements to a file
            output_file.write(sql_insert + '\n')
             

mfile.close()
output_file.close()