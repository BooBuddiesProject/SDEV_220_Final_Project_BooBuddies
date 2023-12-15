import pandas as pd
import geopy as gp
from geopy import distance
class Recommendation:

    def __init__(self, newRec):
        self.placeID = newRec["placeID"]
        self.cuisine = newRec["Rcuisine"]
        self.rating = newRec["rating"]
        self.latitude = newRec["latitude"]
        self.longitude = newRec["longitude"]
        self.name = newRec["name"]
        self.price = newRec["price"]
        self.ranking = newRec["ranking"]
        self.address = newRec["address"]
        self.city = newRec["city"]
        self.state = newRec["state"]
        

def get_recs(df, args, p1):
    cuisine_option = args.get("search_Foodtype", "All")
    if cuisine_option == "All":
        results = df.data
    else:
        results = df.data[df.data["Rcuisine"].str.contains(cuisine_option)]

    recs = []
    for result in results.to_dict("records"):
        resultcord = (result["latitude"],result["longitude"])
        miles = distance.distance(resultcord, p1).miles
        result["ranking"] = ranking(miles, result["rating"])
        recs.append(Recommendation(result))
      
    recs.sort(key = lambda x: x.ranking, reverse = True)

    return recs
    
def ranking(miles, rating):

    return (miles * .01) + (int(rating) * .99)
