
import utm
import unidecode
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent="geocode",timeout=3)
busca =  RateLimiter(geolocator.geocode, min_delay_seconds=1, max_retries=8)

def buscanominatim(query):
    try:
        retornonominatim = busca(query)
    except:
        return  None
    else:
        if retornonominatim:
            retornonominatim = (retornonominatim).raw
            retornonominatim["display_name"] = unidecode.unidecode(retornonominatim["display_name"])
            retornonominatim["relevance"] = retornonominatim["importance"]
            retornonominatim["licence"] = unidecode.unidecode(retornonominatim["licence"])
            utmgeo = utm.from_latlon(float(retornonominatim["lat"]),float(retornonominatim["lon"]))
            retornonominatim["utme"] = utmgeo[0]
            retornonominatim["utmn"] = utmgeo[1]
            retornonominatim["utmfuso"] = utmgeo[2]
            retornonominatim["utmzone"] = utmgeo[3]
            retornonominatim["geocoder"] = "Nominatim"
            return retornonominatim
        else:
            return  None