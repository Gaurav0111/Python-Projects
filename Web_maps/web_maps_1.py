from subprocess import Popen
from textwrap import fill
from tkinter.tix import PopupMenu
from turtle import circle, color, fillcolor
from xml.etree.ElementPath import get_parent_map
import folium
import pandas

# creating a layer of map
map = folium.Map(location=[29.1175481,79.5028568],zoom_start=6) #tiles="Mapbox Bright" ) 







# # creating a mark on map
# fg.add_child(folium.Marker(location=[29.1175481,79.5028568] , popup=' HEy its my home ' , icon= folium.Icon(color="green")))  

#adding marker using for loop
# for coordinates in ([29.1175481,79.5028568],[28.11,70.50],[29.10,79.51]):
    # fg.add_child(folium.Marker(location=coordinates , popup=' HEy its my home ' , icon= folium.Icon(color="green")))



#importing a file to get the dat for latitude and longitude
df = pandas.read_csv("address.txt")

# getting any latitude and longitude from data
lat = list(df["LAT"])
lon = list(df["LON"])
loc = list(df["LOCATION"])


# creating function for giving different colors to pop_up 
def popup_color(loc):
    if loc[4]=="a":
        return "orange"
    else:
        return "blue"
    # return "green"


# creating markers according to the data given in sheet
# for lt,ln,lc in zip(lat,lon,loc) :
    # fg.add_child(folium.Marker(location=[lt,ln] , popup=lc  , icon= folium.Icon(color=popup_color(lc))))

fg = folium.FeatureGroup(name='popup')

# changing the logo of pop-up to circle
for lt,ln,lc in zip(lat,lon,loc) :
    fg.add_child(folium.CircleMarker(location=[lt,ln] , radius=6 , popup=str(lc)  , fillcolor=popup_color(lc) , color=popup_color(lc) , opacity = 0.9,fill=True ))


# addign a layer of polygon over the map
# fg.add_child(folium.GeoJson(data=open('world.json' , 'r' , encoding='utf-8-sig').read()))


fg1 = folium.FeatureGroup(name='Population')

# adding different colours to the polygon according to the population of the country ,data is taken from 'world.jason ' file
fg1.add_child(folium.GeoJson(data=open('world.json' , 'r' , encoding='utf-8-sig').read() , style_function= lambda x: {'fillColor' : 'green' if x ['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))



map.add_child(fg)
map.add_child(fg1)


# adding an option for user to custom the layer accordingly
map.add_child(folium.LayerControl())


# saving it as a html file
map.save("uttarakhand.html")

