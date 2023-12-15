import geopy as gp

class Geolocation:
    

    def __init__(self,search_term):

        self.loc = gp.Nominatim(user_agent="Boolocate")
        self.location = self.loc.geocode(search_term)
        self.p1 = (self.location.latitude, self.location.longitude)


        