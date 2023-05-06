import requests
import json

print("Bienvenido a la API de Clash of Clans.") 
print("Esta API, hará una busqueda que nos podrá mostrará datos de un solo jugador en función de su código.")
print("Además también tenemos un buscador de clanes según algunos parámetros como pueden ser, el nombre del clan, frecuencia de guerra, \nminimo y máximo de integrantes del clan, nivel del clan e incluso un límite de número de clanes a mostrar por pantalla.")
print("Con esto, os dejo en vuestras manos este grandioso poder.")
print("------------------------------------------------------------")

codigo_jugador = input("Introduce el código sin # del jugador de Clash of Clans: ")

url = F'https://api.clashofclans.com/v1/players/%23{codigo_jugador}'
token = 'Bearer [INTRODUCE_TU_TOKEN]'

headers = {'Authorization': token}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f'Error en la búsqueda del jugador. Problema: {response.status_code} - {response.text}')

print("Estos son todos los datos del jugador",codigo_jugador)


nombre_clan = input("Introduce el nombre del clan de Clash of clans: ")
frecuencia_guerra = input("Introduce la frecuencia de guerra del clan de Clash of clans: ")
numero_miembros_min = int(input("Introduce el número de jugadores que tiene el clan de Clash of clans que quieres buscar como mínimo: "))
numero_miembros_max = int(input("Introduce el número de jugadores que tiene el clan de Clash of clans que quieres buscar como máximo: "))
nivel_clan = input("Introduce el nivel del clan de Clash of clans: ")
num_clanes_a_mostrar = input("Introduce el número máximo de clanes a mostrar de Clash of clans: ")

url = F'https://api.clashofclans.com/v1/clans?name={nombre_clan}&warFrequency={frecuencia_guerra}&minMembers={numero_miembros_min}&maxMembers={numero_miembros_max}&minClanLevel={nivel_clan}&limit={num_clanes_a_mostrar}'
token = 'Bearer [INTRODUCE_TU_TOKEN]'

headers = {'Authorization': token}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f'Error en la búsqueda del jugador. Problema: {response.status_code} - {response.text}')
