import folium #to do webmapping python

import pandas as pd
import json



#to read csv val in the map
x=pd.read_csv('C:\Python27\Lokesh\india_cities_coord.csv')

#gives the val in the col lat,long,population
lat=x['lat']
lon=x['long']
pop=x['population']

#def color_producer():
    

#latitude,longtitude,with zoom value being entered
map=folium.Map(location=[20.5937,78.9629],zoom_start=15,tiles='Stamen Terrain')


#adding markers in desired location

#using for loop multiple markers can be added in desired loc and zip func is used to iterate multiple lists
for lt, ln, p in zip(lat, lon, pop):
    map.circle_marker([lt,ln],radius=6,fill_opacity=0.8, popup=str(p))

#popup takes oly string values, now each markers show their population in respective cities

map.geo_json(data=(open('C:\Python27\Lokesh\world.json','r',encoding='utf-8-sig')))


#map is being created but inorder to view convert into html r respective files
map.create_map(path='C:\Python27\Lokesh\Mapping\map.html')

