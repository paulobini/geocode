#ESCRITO POR PAULO BINI 08-12-2021
from os import replace
import requests
import json
from requests.models import Response
from requests import Session
from requests.auth import HTTPBasicAuth
import utm
import unidecode


#MapBox
apimapbox = 'https://api.mapbox.com/geocoding/v5/mapbox.places/'
mapboxmiddle = '.json?access_token='
mapboxtoken = 'pk.eyJ1IjoicGF1bG9iaW5pIiwiYSI6ImNrd3hqYXlhbjBlc2wyd2xhejFveHV5NWcifQ.qSi8zTGL_caE_sRih003eg'


def buscamapbox(end):
    try:
        retornomapbox = requests.get(apimapbox+end+mapboxmiddle+mapboxtoken)
        print(end)
    except:
        return  None
    else:
        if retornomapbox:
            if '"features":[]' in retornomapbox.text:
                return None
            else:
                retorno = json.loads(unidecode.unidecode(retornomapbox.text))
                properties = retorno["features"][0]['properties']
                properties['attribution'] = retorno["attribution"]
                properties['place_name'] = retorno["features"][0]['place_name']
                properties['relevance'] = retorno["features"][0]['relevance']
                geometry = retorno["features"][0]['geometry']['coordinates']
                latitude = geometry[1]
                longitude = geometry[0]
                utmgeo = utm.from_latlon(float(latitude),float(longitude))
                properties['lat'] = str(latitude)
                properties['lon'] = str(longitude)
                properties["utme"] = utmgeo[0]
                properties["utmn"] = utmgeo[1]
                properties["utmfuso"] = utmgeo[2]
                properties["utmzone"] = utmgeo[3]
                properties["geocoder"] = "MapBox"
                return properties
        else:
            return  None