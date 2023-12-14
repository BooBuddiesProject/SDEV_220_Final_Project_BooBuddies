import pandas as pd

class Recommendation:

    def __init__(self, placeID, cuisine, rating, latitude, longitude, name, price):
        self.placeID = placeID
        self.cuisine = cuisine
        self.rating = rating
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.price = price

def get_recs(df, cuisine_option):
    results = df.data[df.data["Rcuisine"].str.contains(cuisine_option)]