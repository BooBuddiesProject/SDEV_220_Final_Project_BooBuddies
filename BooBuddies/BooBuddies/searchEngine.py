import pandas as pd

#need to add an input to search page taking string values in a tuple

#test should print payment hours and parking csv data using radials
search_Parameters = []

def search_Data():
    search_result = pd.read_csv("BooBuddies/empty.csv")

    for parameter in search_Parameters:
        #going through the different types of data
        if parameter == "payment":
            payment_data = pd.read_csv("Restaurant/chefmozaccepts.csv", index_col="placeID")
            search_result += payment_data
            continue

        elif parameter == "cuisine":
            cuisine_data = pd.read_csv("Restaurant/chefmozcuisine.csv", index_col="placeID")
            search_result += cuisine_data
            continue

        elif parameter == "hours":
            hours_data = pd.read_csv("Restaurant/chefmozhours4.csv", index_col="placeID")
            search_result += hours_data
            continue

        elif parameter == "parking":
            parking_data = pd.read_csv("Restaurant/chefmozparking.csv", index_col="placeID")
            search_result += parking_data
            continue

        elif parameter == "location":
            location_data = pd.read_csv("Restaurant/geoplaces2.csv", index_col="placeID")
            search_result += location_data
            continue

        elif parameter == "rating":
            rating_data = pd.read_csv("Restaurant/rating_final.csv", index_col="placeID")
            search_result += rating_data
            continue

        #print out the result for testing
        print(search_result)

search_Data()

