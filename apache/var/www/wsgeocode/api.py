import os
import utm
from typing import Tuple
import flask
import unidecode
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from flask import request, jsonify
from geopy.location import Location

def set_proxy():
    proxy_addr = 'http://srvxpro:80'.format(
        address='srvxpro', port=int('80'))
    os.environ['http_proxy'] = proxy_addr
    os.environ['https_proxy'] = proxy_addr

def unset_proxy():
    os.environ.pop('http_proxy')
    os.environ.pop('https_proxy')

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return 'WSGEOCODE<br/><br/>WebService de geolocalizacao<br/><br/>Os parametros validos para consulta sao:<br/>numero<br/>rua<br/>cidade<br/>estado<br/>pais<br/>cep<br/><br/>exemplo<br/>http://wsgeocode/api/v1/geocode?numero=345&rua=Professor Frederico Herman Junior&cidade=Sao Paulo&estado=Sao Paulo&pais=brazil&cep=05429000'

@app.route('/api/v1/geocode/all', methods=['GET'])
def api_all():
    return jsonify()


@app.route('/api/v1/geocode', methods=['GET'])
def api_endereco():
    
    street = {}
    query = {}
    
    #Verifica se existem parametros elegíveis de busca
    #Se houver, selecina esses dados
    
    
    if 'numero' in request.args:
        numero = str(request.args['numero'])
        street["housenumber"] = numero
    if 'rua' in request.args:
        rua = str(request.args['rua'])
        street["streetname"] = rua
        if 'numero' in request.args:
            query["street"] = str(street["housenumber"]+" "+street['streetname'])
        else:
            query["street"] = str(street['streetname'])
    if 'cidade' in request.args:
        cidade = str(request.args['cidade'])
        query["city"] = cidade
    if 'estado' in request.args:
        estado = str(request.args['estado'])
        query["state"] = estado
    if 'pais' in request.args:
        pais = str(request.args['pais'])
        query["country"] = pais
    if 'cep' in request.args:
        cep = str(request.args['cep'])
        if len(cep) == 8:
            query["postalcode"] = '{}-{}'.format(cep[0:5], cep[5:8])
    
    results = []

    #Realiza a consulta com base nos parametros coletados
    #Adiciona a saida da consulta temporariamente
    
    set_proxy()
    geolocator = Nominatim(user_agent="geocode",timeout=3)
    busca =  RateLimiter(geolocator.geocode, min_delay_seconds=1, max_retries=8)
    retorno = busca(query)
    unset_proxy()

    if retorno:
        retorno = (retorno).raw
    else:
        return ('Os parametros informados na consulta nao retornaram informacoes validas')

    retorno["display_name"] = unidecode.unidecode(retorno["display_name"])
    retorno["licence"] = unidecode.unidecode(retorno["licence"])
    utmgeo = utm.from_latlon(float(retorno["lat"]),float(retorno["lon"]))
    retorno["utme"] = utmgeo[0]
    retorno["utmn"] = utmgeo[1]
    retorno["utmfuso"] = utmgeo[2]
    retorno["utmzone"] = utmgeo[3]
    
    results.append(retorno)
    # Usa a função jsonify do Flask para converter a lista de resultados
    
    return jsonify(results)
    

application = app

if __name__ == '__main__':
    app.run()