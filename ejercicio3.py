import requests
import json

print("Bienvenido a la API de Clash of Clans.") 
print("Este ejercicio 3, hará una busqueda que nos podrá mostrará el nivel de experiencia, las copas actuales y su record de copas (en las 2 aldeas),\ny mostrará el nivel de las tropas del jugador en función de su código.")
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
    nivel_experiencia = json['expLevel']
    copas_actuales_normal = json['trophies']
    copas_actuales_nocturna = json['versusTrophies']
    mejor_nivel_copas = json['bestTrophies']
    mejor_nivel_copas_nocturna = json['bestVersusTrophies']

    print(f'{nombre} tiene {nivel_experiencia} niveles de experencia.')
    print(f'{nombre} tiene actualmente en la aldea normal {copas_actuales_normal} y en la aldea nocturna {copas_actuales_nocturna}. \nEl record de copas en la aldea normal es de {mejor_nivel_copas} y de la aldea nocturna {mejor_nivel_copas_nocturna}.')
    print(f'El nivel de las tropas de {nombre} es el siguiente')
    for troop in json['troops']:
        print(f"Nombre de la tropa: {troop['name']} -> {troop['level']}")

else:
    print(f'Error en la búsqueda del jugador. Problema: {response.status_code} - {response.text}')

print("Estos son todos los datos del jugador",codigo_jugador)