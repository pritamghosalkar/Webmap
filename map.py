import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def icon_color(elevation):
    if elevation < 2000:
        return 'green'
    elif 2000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
map = folium.Map(location=[38,-99], zoom_start=3)

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(location=[lt,ln],popup=str(el)+"m",icon=folium.Icon(color=icon_color(el))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<1000000
else 'orange' if 1000000<=x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("map.html")
