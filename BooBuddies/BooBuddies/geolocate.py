import geopy as gp

loc = gp.Nominatim(user_agent="Boolocate")

#enter the location name prefered city name
get_loc = loc.geocode()

print(get_loc.address)
print(get_loc.latitude)
print(get_loc.longitude)

