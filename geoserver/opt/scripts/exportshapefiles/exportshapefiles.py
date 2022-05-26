import shapefile
from sys import platform
import os
import pyodbc
import shutil
from unidecode import unidecode

shpfiles = os.path.join(os.getcwd(),'empreendimentos/','empreendimentos')

dirempreendimentos = (os.path.join(os.getcwd(),'empreendimentos/'))
destdir = "/opt/geodata/shape/empreendimentos/"
#destdir = "/home/bini/GIT/geocode/geoserver/opt/scripts/exportshapefiles/teste/"

server = '10.25.192.65,1433'
database = 'DBGEOEMPRS'
username = 'usugeomaps'
password = 'U$uge0map$'
driverlinux = 'ODBC Driver 17 for SQL Server'
driverwin = 'SQL Server Native Client 11.0'


#CRIAÇÃO DA STRING DE CONEXÃO
if platform == 'linux':
    driver = driverlinux
if platform == 'win32':
    driver = driverwin

cnxn = pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+';autocommit=True')
cursor1 = cnxn.cursor()
cont = 1
rows = cursor1.execute("SELECT DRAZAOSOCIL, latitude, longitude, nmuncp, nseqnc, dmuncp FROM TB_EMPRSGEO").fetchall()

if os.path.exists(dirempreendimentos):
    shutil.rmtree(dirempreendimentos)

with shapefile.Writer (shpfiles) as w:
    w.field('PK', 'C')
    w.field('DRAZAOSOCI', 'C')
    w.field('latitude', 'C')
    w.field('longitude', 'C')
    w.field('nmuncp', 'C')
    w.field('nsecnc', 'C')
    w.field('dmuncp', 'C')

    for row in rows:
        linha = []
        linha.append(str(cont))
        if row[0]:
            linha.append(unidecode(row[0]))
        else:
            linha.append("")
        
        if row[1]:
            linha.append(float(row[1]))
        else:
            linha.append("")

        if row[2]:
            linha.append(float(row[2]))
        else:
            linha.append("")
        
        if row[3]:
            linha.append(row[3])
        else:
            linha.append("")
        
        if row[4]:
            linha.append(row[4])
        else:
            linha.append("")

        if row[5]:
            linha.append(unidecode(row[5]))
        else:
            linha.append("")

        if linha[2] != "" and linha[3] != "":
            w.point(linha[3],linha[2])
            w.record(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6])
        cont = cont+1

prj = open("%s.prj" % shpfiles, "w")
epsg = 'GEOGCS["WGS 84",'
epsg += 'DATUM["WGS_1984",'
epsg += 'SPHEROID["WGS 84",6378137,298.257223563]]'
epsg += ',PRIMEM["Greenwich",0],'
epsg += 'UNIT["degree",0.0174532925199433]]'
prj.write(epsg)
prj.close()

for arquivo in os.listdir(dirempreendimentos):
    origem = (dirempreendimentos+arquivo)
    destino = (destdir+arquivo)
    if os.path.isfile(origem):
        shutil.copy2(origem,destino)