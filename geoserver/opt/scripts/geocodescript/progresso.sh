#!/bin/bash
sucesso=
processado=
total=
percentsucesso=
percenttotal=

total=$(cat /opt/scripts/geocodescript/log/*log* | grep "FORAM ENCONTRADOS" | tail -n 1 |awk '{print $6}')

sucesso=$(cat /opt/scripts/geocodescript/log/*log* | grep LATITUDE | wc -l)
processado=$(cat /opt/scripts/geocodescript/log/*log* | wc -l)

nominatim=$(cat /opt/scripts/geocodescript/log/*log* | grep Nominatim | wc -l)
traveltime=$(cat /opt/scripts/geocodescript/log/*log* | grep TravelTime | wc -l)
mapbox=$(cat /opt/scripts/geocodescript/log/*log* | grep MapBox | wc -l)


percentsucesso=$(echo "$sucesso * 100 / $processado" | bc)
percenttotal=$(echo "$processado * 100 / $total" | bc)
percentnominatim=$(echo "$nominatim * 100 / $processado" | bc)
percenttraveltime=$(echo "$traveltime * 100 / $processado" | bc)
percentmapbox=$(echo "$mapbox * 100 / $processado" | bc)

echo "Por hora temos $percentsucesso% de sucesso no Geocode"
echo "Geocoders: $percentnominatim% Nominatim, $percenttraveltime% TravelTime, $percentmapbox% MapBox"
echo "De um total de $total empreendimentos, $processado foram processados"
echo "O progresso da execução é de $percenttotal% do total"