#ESCRITO POR PAULO BINI 27-10-2021
import pyodbc
from sys import platform

#DADOS DA CONEXÃO ODBC
server = '10.25.192.65,1433'
database = 'DBGEOEMPRS'
username = 'usugeomaps'
password = 'U$uge0map$'
driverlinux = 'ODBC Driver 18 for SQL Server'
driverwin = 'SQL Server Native Client 11.0'

#CRIAÇÃO DA STRING DE CONEXÃO
if platform == 'linux':
    driver = driverlinux
if platform == 'win32':
    driver = driverwin

cnxn = pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+';autocommit=True;encrypt=no;trust_server_certificate=no')

cursor1 = cnxn.cursor()
cursor2= cnxn.cursor()

def registrosafetados(antque):
    #registros = cursor1.execute("SELECT COUNT(*) FROM TB_EMPRSGEO where (DATULTMATULZ > ? or DATULTMATULZ is null) or (latitude is null or longitude is null)",antque).fetchone()
    registros = cursor1.execute("SELECT COUNT(*) FROM TB_EMPRSGEO where (DATULTMATULZ is null) and (latitude is null or longitude is null)").fetchone()
    #registros = cursor1.execute("SELECT COUNT(*) FROM TB_EMPRSGEO where (DATULTMATULZ < ? or DATULTMATULZ is null) or (latitude is null or longitude is null)",antque).fetchone()
    #registros = cursor1.execute("SELECT COUNT(*) FROM TB_EMPRSGEO where (DATULTMATULZ < ? or DATULTMATULZ is null) and (latitude is null or longitude is null)",antque).fetchone()
    #registros = cursor1.execute("SELECT COUNT(*) FROM TB_EMPRSGEO where latitude is null or longitude is null").fetchone()
    registros = registros[0]
    return registros

def select(antque):
    #rows = cursor1.execute("SELECT NSEQNC,NLOGRD,DLOGRD,DMUNCP,CCEP,DATULTMATULZ,DRAZAOSOCIL,NMUNCP,DBAIRR FROM TB_EMPRSGEO where (DATULTMATULZ > ? or DATULTMATULZ is null) or (latitude is null or longitude is null)",antque).fetchall()
    rows = cursor1.execute("SELECT NSEQNC,NLOGRD,DLOGRD,DMUNCP,CCEP,DATULTMATULZ,DRAZAOSOCIL,NMUNCP,DBAIRR FROM TB_EMPRSGEO where (DATULTMATULZ is null) and (latitude is null or longitude is null)").fetchall()
    #rows = cursor1.execute("SELECT NSEQNC,NLOGRD,DLOGRD,DMUNCP,CCEP,DATULTMATULZ,DRAZAOSOCIL,NMUNCP,DBAIRR FROM TB_EMPRSGEO where (DATULTMATULZ < ? or DATULTMATULZ is null) or (latitude is null or longitude is null)",antque).fetchall()
    #rows = cursor1.execute("SELECT NSEQNC,NLOGRD,DLOGRD,DMUNCP,CCEP,DATULTMATULZ,DRAZAOSOCIL,NMUNCP FROM TB_EMPRSGEO where (DATULTMATULZ < ? or DATULTMATULZ is null) and (latitude is null or longitude is null)",antque).fetchall()
    #rows = cursor1.execute("SELECT NSEQNC,NLOGRD,DLOGRD,DMUNCP,CCEP,DATULTMATULZ,DRAZAOSOCIL,NMUNCP FROM TB_EMPRSGEO where latitude is null or longitude is null").fetchall()
    return rows

def updatesemdadosgeo(agora,nseqnc,nmuncp):
    cursor2.execute("UPDATE TB_EMPRSGEO SET TB_EMPRSGEO.DATULTMATULZ = ? where NSEQNC = ? and NMUNCP = ?",agora,nseqnc,nmuncp)
    cursor2.commit()

def updatecomdadosgeo(lat,lon,utme,utmn,utmfuso,utmzone,agora,nseqnc,nmuncp):
    cursor2.execute("UPDATE TB_EMPRSGEO SET TB_EMPRSGEO.latitude = ? , TB_EMPRSGEO.longitude = ? , TB_EMPRSGEO.QUTME = ? , TB_EMPRSGEO.QUTMN = ? , TB_EMPRSGEO.IFUSO = ? , TB_EMPRSGEO.izone = ? , TB_EMPRSGEO.DATULTMATULZ = ? where NSEQNC = ? and NMUNCP = ? ",lat,lon,utme,utmn,utmfuso,utmzone,agora,nseqnc,nmuncp)
    cursor2.commit()