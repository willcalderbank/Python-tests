from geopy import geocoders
import math
import sys
import logging

def get_location_from_postcode(postcode):
    logger = logging.getLogger("general_logger")
    g = geocoders.Google()
    try:
        place, (latitude, longitude) = g.geocode(postcode)
        logger.debug("%s: %.5f, %.5f" % (place, latitude, longitude))
        return (place,(latitude, longitude))
    except ValueError:
        logger.debug("Identification failed" + postcode)
    except geocoders.google.GQueryError:
        logger.debug("Google couldnt find this " + postcode)
    except geocoders.google.GTooManyQueriesError:
        logger.error("Google is not allowing us to hit their search any more " + postcode)
    return (None,(None,None))
        

'''
Calculates distance between two longitudes and latitudes, returns distance in km
'''
def calculate_distance((lat1,lon1), (lat2,lon2)):
    R = 6371 # km
    dLat = math.radians(math.fabs(lat2-lat1))
    dLon = math.radians(math.fabs(lon2-lon1))
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2) 
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

'''
Helper class distance between two postcodes, returns distance in km
'''
def calculate_distance_postcode(postcode1,postcode2):
    return calculate_distance(get_location_from_postcode(postcode1)[1], get_location_from_postcode(postcode2)[1])

def km_to_miles(km):
    return km * 1.609344

def miles_to_km(miles):
    return miles / 1.609344

