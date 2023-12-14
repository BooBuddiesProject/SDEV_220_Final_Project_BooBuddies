import csv
import pandas as pd
from pathlib import Path
# import os

datapath = "./BooBuddies/data/"

def foodtypes_list():
    # cwd = os.getcwd()
    # print(cwd)

    filename = Path(__file__).parent / "data/foodtypes.csv"

    file = open(filename,"r")
    # type(file)
    data = list(csv.reader(file, delimiter=","))
    rows = []
    for row in data:
        rows.append(row)
        
    file.close()
    return(rows)

def search_Cuisine(keyword ):
    print("This is what was passed in: "+ keyword)
    df = pd.read_csv(datapath+"chefmozcuisine.csv")
    
    filtered_df = df["Rcuisine"] 

    nomatch = "No Match Was Found"

    for item in filtered_df:
        print("ListItem:" + item)
        if item == keyword.lower():
            search_result = item
            noresult = "False"
            return keyword
                    
        else:
            noresult = "True"
            continue

    if noresult == "True":
        print(nomatch)
                    
    else:
        print("Item Found: " + search_result)
    
