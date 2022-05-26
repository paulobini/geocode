import csv
from sys import platform
import os
import pyodbc

rootpath = os.getcwd()
mycsvfile = os.path.join(rootpath,'TBEMPRSGEO.csv')

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
rows = cursor1.execute("SELECT * FROM TB_EMPRSGEO").fetchall()
with open(mycsvfile, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter =';')
    linha1 = []
    linha1.append('PK')
    x = 0
    for i in cursor1.description:
        linha1.append(cursor1.description[x][0])
        x = x+1
    writer.writerow(linha1)
    for row in rows:
        linha = []
        linha.append(str(cont))
        if row[0]:
            linha.append(row[0])
        else:
            linha.append("")

        if row[1]:
            linha.append(row[1])
        else:
            linha.append("")
        
        if row[2]:
            linha.append(row[2])
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
            linha.append(row[5])
        else:
            linha.append("")

        if row[6]:
            linha.append(row[6])
        else:
            linha.append("")

        if row[7]:
            linha.append(row[7])
        else:
            linha.append("")
        
        if row[8]:
            linha.append(row[8])
        else:
            linha.append("")

        if row[9]:
            linha.append(row[9])
        else:
            linha.append("")

        if row[10]:
            linha.append(row[10])
        else:
            linha.append("")

        if row[11]:
            linha.append(row[11])
        else:
            linha.append("")
        
        if row[12]:
            linha.append(row[12])
        else:
            linha.append("")

        if row[13]:
            linha.append(row[13])
        else:
            linha.append("")
        
        if row[14]:
            linha.append(row[14])
        else:
            linha.append("")
        
        if row[15]:
            linha.append(row[15])
        else:
            linha.append("")
        
        if row[16]:
            linha.append(row[16])
        else:
            linha.append("")
        
        writer.writerow(linha)
        cont = cont+1