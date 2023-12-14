import pandas as pd

class DataFrame:
        
        def __init__(self):
            #fixing pandas optons
            pd.options.display.max_columns = None
            pd.options.display.max_rows = None
            pd.options.display.max_colwidth = None

            df_cuisine = pd.read_csv("BooBuddies\Restaurant\chefmozcuisine.csv")
            df_geo = pd.read_csv("BooBuddies\Restaurant\geoplaces2.csv")
            df_rating = pd.read_csv(r"BooBuddies\Restaurant\rating_final.csv")

            #combine the csv's into one dataframe and clean the data
            df_combo = df_cuisine.merge(df_geo, on ="placeID").merge(df_rating, on = "placeID")
            df_combo = df_combo.drop_duplicates(subset=["placeID"])
            df_combo = df_combo.eval("rating = rating + food_rating + service_rating")
            df_combo = df_combo[["placeID","Rcuisine", "rating","latitude", "longitude", "name", "price"]]
            self.data = df_combo

