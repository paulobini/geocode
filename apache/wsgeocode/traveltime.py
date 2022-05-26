#ESCRITO POR PAULO BINI 25-11-2021
import utm
from os import replace
import requests
import json
from requests.models import Response
from requests import Session
from requests.auth import HTTPBasicAuth
import unidecode


#TimeTravel
apitraveltime = 'https://api.traveltimeapp.com/v4/geocoding/search?query='

traveltimeheaders = {
    'Accept': 'application/json',
    'X-Application-Id': 'ee39d23a',
    'X-Api-Key' : 'f10745438628d4f3944e85a49272298c',
    'Accept-Language' : 'pt-BR'
}

def buscatraveltime(end):
    try:
        retornotraveltime = requests.get(apitraveltime+end, headers=traveltimeheaders)
    except:
        return  None
    else:
        if retornotraveltime:
            if retornotraveltime.text == '{"type":"FeatureCollection","features":[]}':
                return None
            else:
                retorno = json.loads(unidecode.unidecode(retornotraveltime.text))
                properties = retorno["features"][0]['properties']
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
                properties["geocoder"] = "TravelTime"
                properties["relevance"] = properties["score"]
                return properties
        else:
            return  None