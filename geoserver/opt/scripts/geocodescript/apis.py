#ESCRITO POR PAULO BINI 27-10-2021
import zeep
import requests
import json
from zeep import Client
from decimal import Decimal

#Relevância mínima do resultado para a inserção no banco
minrelevance = 0.6

#CORREIOS
apicorreios = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'

clientcorreios = Client(wsdl=apicorreios)

#WSGEOCODE
wsgeocode = "http://wsgeocode/api/v1/geocode"



def buscacorreios(cep):
    try:
        retornocorreios = clientcorreios.service.consultaCEP(cep=cep)
    except:
        return  None
    else:
        if retornocorreios:
            return zeep.helpers.serialize_object(retornocorreios)
        else:
            return  None
    
def buscawsgeocode(endereco):
    try:
        retornowsgeocode = requests.get(wsgeocode, endereco)
    except:
        return  None
    else:
        if retornowsgeocode:
            if retornowsgeocode.text == 'Os parametros informados na consulta nao retornaram informacoes validas':
                return None
            else:
                json_data = json.loads(retornowsgeocode.text)
                coordenadas = {}
                coordenadas["lat"] = json_data[0]["lat"]
                coordenadas["lon"] = json_data[0]["lon"]
                coordenadas["utme"] = json_data[0]["utme"]
                coordenadas["utmn"] = json_data[0]["utmn"]
                coordenadas["utmfuso"] = json_data[0]["utmfuso"]
                coordenadas["utmzone"] = json_data[0]["utmzone"]
                coordenadas["geocoder"] = json_data[0]["geocoder"]
                coordenadas["relevance"] = json_data[0]["relevance"]
                if Decimal(coordenadas["relevance"]) >= minrelevance:
                    return coordenadas
                else:
                    return None
        else:
            return  None