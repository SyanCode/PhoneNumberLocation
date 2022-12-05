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
print("Pays : " + localisation)

# Trouver l'opérateur
operator = phonenumbers.parse(num)
print("Opérateur : " + carrier.name_for_number(operator,"fr"))

# Trouver la latitude/longitude
key = api_key_opencage
coords = OpenCageGeocode(key)
request = str(localisation)
answer = coords.geocode(request)
lat = answer[0]["geometry"]["lat"]
lng = answer[0]["geometry"]["lng"]
print("Latitude : " + str(lat))
print("Longitude : " + str(lng))

# Création de la Map
Map = folium.Map(location=[lat, lng], zoom_start=12)
folium.Marker([lat, lng], popup=localisation).add_to(Map)
Map.save("map" + num + ".html")

# Message de fin
print("La map a été chargée dans le projet en format html.")