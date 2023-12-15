import pandas as pd

class Recommendation:

    def __init__(self, newRec):
        self.placeID = newRec["placeID"]
        self.cuisine = newRec["Rcuisine"]
        self.rating = newRec["rating"]
        self.latitude = newRec["latitude"]
        self.longitude = newRec["longitude"]
        self.name = newRec["name"]
        self.price = newRec["price"]

def get_recs(df, args):
    cuisine_option = args.get("search_Foodtype", "All")
    if cuisine_option == "All":
        results = df.data
    else:
        results = df.data[df.data["Rcuisine"].str.contains(cuisine_option)]

    recs = []
    for result in results.to_dict("records"):
      recs.append(Recommendation(result))
      
    return recs
    