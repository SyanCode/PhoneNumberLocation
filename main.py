# Appel de dotenv pour cacher la clé d'API d'OpenCage
import os, sys
from dotenv import load_dotenv
load_dotenv()

api_key_opencage = os.getenv("API_KEY_OPENCAGE")

# Modules
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Trouver le pays du numéro
num = input("Entrer un numéro de téléphone français (format +33) : ")
monNum = phonenumbers.parse(num)
localisation = geocoder.description_for_number(monNum,"fr")

# Trouver l'opérateur du numéro
operator = phonenumbers.parse(num)

# Trouver la latitude/longitude
key = api_key_opencage
coords = OpenCageGeocode(key)
request = str(localisation)
answer = coords.geocode(request)
lat = answer[0]["geometry"]["lat"]
lng = answer[0]["geometry"]["lng"]

# Création de la Map
Map = folium.Map(location=[lat, lng], zoom_start=12)
folium.Marker([lat, lng], popup=localisation).add_to(Map)

# Prints des informations

# Pays
print("Pays : " + localisation)
# Opérateur
print("Opérateur : " + carrier.name_for_number(operator,"fr"))
# Latitude/Longitude
print("Latitude : " + str(lat))
print("Longitude : " + str(lng))
# Map save
Map.save("map" + num + ".html")
# Print à titre informatif
print("La map a été chargée dans le projet sous le nom de map" + num + ".html.")