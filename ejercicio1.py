import requests
import json

print("Bienvenido a la API de Clash of Clans.") 
print("Este ejercicio 1, hará una busqueda que nos podrá mostrará el nombre y el nivel del ayuntamiento \nde la aldea normal y la nocturna de un solo jugador en función de su código.")
print("Con esto, os dejo en vuestras manos este grandioso poder.")
print("------------------------------------------------------------")

codigo_jugador = input("Introduce el código sin # del jugador de Clash of Clans: ")

url = F'https://api.clashofclans.com/v1/players/%23{codigo_jugador}'
token = 'Bearer [INTRODUCE_TU_TOKEN]'

headers = {'Authorization': token}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    json= response.json()
    nombre = json['name']
    nivel_ayuntamiento = json['townHallLevel']
    nivel_ayuntamiento_nocturna = json['builderHallLevel']
    print(f'El nombre del jugador es {nombre}, su nivel de ayuntamiento en su cuenta es {nivel_ayuntamiento} y de la aldea nocturna es {nivel_ayuntamiento_nocturna}')
else:
    print(f'Error en la búsqueda del jugador. Problema: {response.status_code} - {response.text}')

print("Estos son todos los datos del jugador",codigo_jugador)
