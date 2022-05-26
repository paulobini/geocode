#ESCRITO POR PAULO BINI 27-10-2021
from attr import asdict
from requests.api import request
from datetime import datetime, timedelta
from requests.sessions import Session
from apis import buscacorreios, buscawsgeocode
from sql import registrosafetados, select, updatesemdadosgeo, updatecomdadosgeo
from log import addlog
import os
import unidecode
import re

addlog('------------------INICIANDO A EXECUCAO DO SCRIPT----------------------------')

#ARQUIVO QUE CONTÉM A PERIODICIDADE DAS ATUALIZAÇÕES, ATUALIZADO AS INFORMAÇÕES MAIS ANTIGAS QUE X DIAS
rootpath = os.getcwd()
lastfile = os.path.join(rootpath,'last.txt')

with open(lastfile) as file:
    last = file.read().replace('\n', '')
antque = datetime.now() - timedelta(days=int(last))
addlog('------------------TRATANDO OS REGISTROS COM ATUALIZACAO ANTERIOR A '+str(antque)+'---------------------')


#DESCOBRE QUANTOS REGISTROS ESTAO DESATUALIZADOS
registros = registrosafetados(antque)
addlog('------------------FORAM ENCONTRADOS '+str(registros)+' REGISTROS PARA ATUALIZACAO---------------------')

#LÊ TODOS OS REGISTROS COM ATUALIZAÇÃO INFERIOR AO PERIODO DEFINIDO
rows = select(antque)
count=0
#PARA CADA REGISTRO RETORNADO, É EXECUTADA A ROTINA ABAIXO
for row in rows:
    agora = datetime.now()
    percent = 0
    count += 1
    percent = round(count*100/registros, 2)
    endereco = {}
    endereco["pais"] = "brasil"
    nseqnc = row[0]
    if row[1]:
        if re.match(r"[-+]?\d+(\.0*)?$",str.strip(row[1])):
            endereco["numero"] = str.strip(row[1])
    if row[2]:
        endereco["rua"] = str.strip(row[2])
        endereco["rua"] = unidecode.unidecode(endereco["rua"])
    if row[3]:
        endereco["cidade"] = str.strip(row[3])
        endereco["cidade"] = unidecode.unidecode(endereco["cidade"])
    if row[4]:
        if len(str(row[4])) == 8:
            endereco["cep"] = row[4]
        elif len(str(row[4])) == 7:
            endereco["cep"] = ('0'+str(row[4]))
        elif len(str(row[4])) == 6:
            endereco["cep"] = ('00'+str(row[4]))
    if row[6]:
        razaosocial = str.strip(row[6])
        razaosocial = unidecode.unidecode(razaosocial)
    else:
        razaosocial = "sem razao social"
    if row[7]:
        nmuncp = row[7]
    if row[8]:
        endereco["bairro"] = str.strip(row[8])
        endereco["bairro"] = unidecode.unidecode(endereco["bairro"])

    #FAZ A CONSULTA NO WEBSERVICE, PASSANDO UM JSON CONTENDO OS DADOS COLETADOS NO REGISTRO
    retornowsgeocode = buscawsgeocode(endereco)
    #SE O WEBSERVICE RETORNAR UMA RESPOSTA VÁLIDA (200), VERIFICA SE HÁ RETORNO DE COORDENADAS, SE NÃO HOUVER É FEITA UMA NOVA TENTATIVA USANDO OS DADOS DE ENDEREÇO DOS CORREIOS, POIS ALGUMAS RUAS PODEM RESULTAR FALHA
    lat = None
    lon = None
    utme = None
    utmn = None
    utmfuso = None
    utmzone = None

    if retornowsgeocode:
        lat = retornowsgeocode['lat']
        lon = retornowsgeocode['lon']
        utme = retornowsgeocode['utme']
        utmn = retornowsgeocode['utmn']
        utmfuso = retornowsgeocode['utmfuso']
        utmzone = retornowsgeocode['utmzone']
        geocoder = retornowsgeocode['geocoder']
        addlog(" "+str(percent)+"% | "+str(geocoder)+" | RAZAO SOCIAL> "+razaosocial+" | LATITUDE> "+str(lat)+" | LOGITUDE> "+str(lon)+" | IMPORTADO DIRETAMENTE")
        updatecomdadosgeo(lat,lon,utme,utmn,utmfuso,utmzone,agora,nseqnc,nmuncp)
    else:
        if  'cep' in endereco:
            if endereco["cep"]:
                cep = endereco["cep"]
            del endereco["cep"]
            retornowsgeocode = buscawsgeocode(endereco)
            if retornowsgeocode:
                lat = retornowsgeocode['lat']
                lon = retornowsgeocode['lon']
                utme = retornowsgeocode['utme']
                utmn = retornowsgeocode['utmn']
                utmfuso = retornowsgeocode['utmfuso']
                utmzone = retornowsgeocode['utmzone']
                geocoder = retornowsgeocode['geocoder']
                addlog(" "+str(percent)+"% | "+str(geocoder)+" | RAZAO SOCIAL> "+razaosocial+" | LATITUDE> "+str(lat)+" | LOGITUDE> "+str(lon)+" | IMPORTADO SEM CEP")
                updatecomdadosgeo(lat,lon,utme,utmn,utmfuso,utmzone,agora,nseqnc,nmuncp)
            else:
                retornocorreios = buscacorreios(cep)
                if retornocorreios:
                    endereco = {}
                    endereco["pais"] = "brasil"
                    if 'cidade' in retornocorreios:
                        if retornocorreios["cidade"]:
                            endereco["cidade"] = unidecode.unidecode(retornocorreios["cidade"])
                    if 'end' in retornocorreios:
                        if retornocorreios["end"]:
                            endereco["rua"] = unidecode.unidecode(retornocorreios["end"])
                    if 'cep' in retornocorreios:
                        if retornocorreios["cep"]:
                            endereco["cep"] = retornocorreios["cep"]
                    retornowsgeocode = buscawsgeocode(endereco)
                    if retornowsgeocode:
                        lat = retornowsgeocode['lat']
                        lon = retornowsgeocode['lon']
                        utme = retornowsgeocode['utme']
                        utmn = retornowsgeocode['utmn']
                        utmfuso = retornowsgeocode['utmfuso']
                        utmzone = retornowsgeocode['utmzone']
                        geocoder = retornowsgeocode['geocoder']
                        addlog(" "+str(percent)+"% | "+str(geocoder)+" | RAZAO SOCIAL> "+razaosocial+" | LATITUDE> "+str(lat)+" | LOGITUDE> "+str(lon)+" | IMPORTADO INF CORREIOS")
                        updatecomdadosgeo(lat,lon,utme,utmn,utmfuso,utmzone,agora,nseqnc,nmuncp)
                    else:
                        retornocorreios = buscacorreios(cep)
                        if retornocorreios:
                            endereco = {}
                            endereco["pais"] = "brasil"
                            if 'cidade' in retornocorreios:
                                if retornocorreios["cidade"]:
                                    endereco["cidade"] = unidecode.unidecode(retornocorreios["cidade"])
                            if 'end' in retornocorreios:
                                if retornocorreios["end"]:
                                    endereco["rua"] = unidecode.unidecode(retornocorreios["end"])
                            retornowsgeocode = buscawsgeocode(endereco)
                            if retornowsgeocode:
                                lat = retornowsgeocode['lat']
                                lon = retornowsgeocode['lon']
                                utme = retornowsgeocode['utme']
                                utmn = retornowsgeocode['utmn']
                                utmfuso = retornowsgeocode['utmfuso']
                                utmzone = retornowsgeocode['utmzone']
                                geocoder = retornowsgeocode['geocoder']
                                addlog(" "+str(percent)+"% | "+str(geocoder)+" | RAZAO SOCIAL> "+razaosocial+" | LATITUDE> "+str(lat)+" | LOGITUDE> "+str(lon)+" | IMPORTADO INF CORREIOS SEM CEP")
                                updatecomdadosgeo(lat,lon,utme,utmn,utmfuso,utmzone,agora,nseqnc,nmuncp)
                            else:
                                addlog(" "+str(percent)+"% | ID> "+str(nseqnc)+" | RAZAO SOCIAL> "+razaosocial+" | >>> nao foram retornados dados de localizacao | NENHUMA RESPOSTA VALIDA")
                                updatecomdadosgeo(lat,lon,utme,utmn,utmfuso,utmzone,agora,nseqnc,nmuncp)
                                #updatesemdadosgeo(agora,nseqnc,nmuncp)
                        else:
                            addlog(" "+str(percent)+"% | ID> "+str(nseqnc)+" | RAZAO SOCIAL> "+razaosocial+" | >>> nao foram retornados dados de localizacao | NENHUMA RESPOSTA VALIDA")
                            updatecomdadosgeo(lat,lon,utme,utmn,utmfuso,utmzone,agora,nseqnc,nmuncp)
                            #updatesemdadosgeo(agora,nseqnc,nmuncp)
                else:
                    addlog(" "+str(percent)+"% | ID> "+str(nseqnc)+" | RAZAO SOCIAL> "+razaosocial+" | >>> nao foram retornados dados de localizacao | CEP INVALIDO NOS CORREIOS")
                    updatecomdadosgeo(lat,lon,utme,utmn,utmfuso,utmzone,agora,nseqnc,nmuncp)
                    #updatesemdadosgeo(agora,nseqnc,nmuncp)
        else:
            addlog(" "+str(percent)+"% | ID> "+str(nseqnc)+" | RAZAO SOCIAL> "+razaosocial+" | >>> nao foram retornados dados de localizacao | RUA E CEP INVALIDOS")
            updatecomdadosgeo(lat,lon,utme,utmn,utmfuso,utmzone,agora,nseqnc,nmuncp)
            #updatesemdadosgeo(agora,nseqnc,nmuncp)

addlog('------------------FINALIZANDO A EXECUCAO DO SCRIPT----------------------------')