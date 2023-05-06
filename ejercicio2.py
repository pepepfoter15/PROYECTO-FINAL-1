import requests
import json

print("Bienvenido a la API de Clash of Clans.") 
print("Este ejercicio 2, hará una busqueda que nos podrá mostrará el nombre del país del clan, los puntos del clan, el número de miembros \ndel clan y nombre de la liga de clanes del clan en cuestión en función de su el nombre del clan, frecuencia de guerra, \nminimo y máximo de integrantes del clan, nivel del clan e incluso un límite de número de clanes a mostrar por pantalla.")
print("Con esto, os dejo en vuestras manos este grandioso poder.")
print("------------------------------------------------------------")

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
    json= response.json()
    nombre_clan = json['items'][0]['name']
    nombre_pais = json['items'][0]['location']['name']
    puntos_clan = json['items'][0]['clanPoints']
    nombre_liga = json['items'][0]['warLeague']['name']
    numero_miembros_del_clan = json['items'][0]['members']
    print(f'El clan {nombre_clan} es del pais {nombre_pais}, con un numero de miembros de {numero_miembros_del_clan}. Además, tiene {puntos_clan} puntos del clan y están en {nombre_liga} en la liga de clanes.')
else:
    print(f'Error en la búsqueda del jugador. Problema: {response.status_code} - {response.text}')
