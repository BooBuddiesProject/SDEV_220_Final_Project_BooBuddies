import csv
# import os

def foodtypes_list():
    # cwd = os.getcwd()
    # print(cwd)

    file = open('./BooBuddies/data/foodtypes.csv',"r")
    # type(file)
    data = list(csv.reader(file, delimiter=","))
    print(data)
    rows = []
    for row in data:
        rows.append(row)
        
    file.close()
    return(rows)
    
