import requests
import json

print("Bienvenido a la API de Clash of Clans.") 
print("Este ejercicio 1, hará una busqueda que nos podrá mostrará el nombre y el nivel del ayuntamiento \nde la aldea normal y la nocturna de un solo jugador en función de su código.")
print("Con esto, os dejo en vuestras manos este grandioso poder.")
print("------------------------------------------------------------")

codigo_jugador = input("Introduce el código sin # del jugador de Clash of Clans: ")

url = F'https://api.clashofclans.com/v1/players/%23{codigo_jugador}'
token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjgwYTBkMzdlLWM5NDktNGQ4OC05NTUyLTAyMzUyNzQxMjBkNSIsImlhdCI6MTY4MzM4NzM5OSwic3ViIjoiZGV2ZWxvcGVyLzg2ODg2OGE0LTc3YTktNzNkZS1mMmY5LWU1ZTljZWQ4NGI5NiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjkwLjE2Ny45OC41OCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.TsdkgTKkFXZYTQgmg44nBDvegM-UyqXno7IA05qux7w_v8I2XBpQP_T2gVueW0K1LLLH5P07cfIZxLKx_yBCdQ'

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