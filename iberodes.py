import pandas as pd
import folium
datos = pd.read_csv('Ibis eremita.csv', sep='\t')
mapa_especie=folium.Map(
                location=[38.002989, -4.641053], 
                zoom_start=6,
                tiles='Mapbox Bright')

for indice, ocurrence in datos.iterrows():
    latitud=ocurrence['decimalLatitude']
    longitud=ocurrence['decimalLongitude']
    if not pd.isnull(latitud):
        punto=folium.Marker(location=[latitud, longitud], 
                     popup='https://www.gbif.org/species/2480770').add_to(mapa_especie)
        
mapa_especie.save ('mapa_ibis_eremita_folium_map.html')