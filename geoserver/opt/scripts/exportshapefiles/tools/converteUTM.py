import utm
retorno = input("Digite as coordenadas LAT, LON")
coordenadas = str.split(str(retorno),', ')
utmgeo = utm.from_latlon(float(coordenadas[0]),float(coordenadas[1]))
print(utmgeo)