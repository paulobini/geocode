from typing import Tuple
import flask
from flask import request, jsonify
from nominatim import buscanominatim
from traveltime import buscatraveltime
from mapbox import buscamapbox

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
    if 'bairro' in request.args:
        bairro = str(request.args['bairro'])
        query["neighborhood"] = bairro
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
    retorno = buscanominatim(query)

    if retorno:
        results.append(retorno)
    else:
        end = ""
        if 'street' in query:
            end = query['street']
        if 'neighborhood' in query:
            end = (end+', '+query['neighborhood'])
        if 'city' in query:
            end = (end+', '+query['city'])
        if 'state' in query:
            end = (end+', '+query['state'])
        if 'postalcode' in query:
            end = (end+', '+str(query['postalcode'])[0:5]+str(query['postalcode'])[6:9])
        if 'country' in query:
            end = (end+', '+query['country'])
        retorno = buscatraveltime(end)
        if retorno:
            results.append(retorno)
        else:
            print(end)
            retorno = buscamapbox(end)
            if retorno:
                results.append(retorno)
            else:
                return ('Os parametros informados na consulta nao retornaram informacoes validas')

    return jsonify(results)

application = app

if __name__ == '__main__':
    app.run()