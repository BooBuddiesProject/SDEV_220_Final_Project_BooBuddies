import geopy as gp

search_term = "South Bend Indiana"


class Geolocation:
    

    def __init__(self,search_term):

        self.loc = gp.Nominatim(user_agent="Boolocate")
        self.location = self.loc.geocode(search_term)
        self.p1 = gp.Point(self.location.latitude, self.location.longitude)
       
loc1 = Geolocation(search_term)

print(loc1.p1)