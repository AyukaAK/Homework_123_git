# Ayuka Kawakami
# June 13, 2022
# Homework 3, Part 1

# On Terminal => LedeProgram % python homework-3-part1-Kawakami.py
# On Terminal => exec(open('homework-3-part1-Kawakami.py').read())


#Q1
#documentation: url = https://pokeapi.co/docs/v2
from itertools import count
import requests

#Get the API and convert Json to the dictionary
response = requests.get('https://pokeapi.co/api/v2/pokemon/55')
print(response)
data = response.json()
print (data)

#Q2: What pokemon has the ID of 55?
print (data.keys())
print (data['name'])
#golduck

#Q3: How tall is that pokemon?
print (data.keys())
print (data['height'])
#17

#Q4 How many versions of Pokemon games have been released?

version_response = requests.get('https://pokeapi.co/api/v2/version-group')
version = version_response.json()

print(f"There are {version['count']} versions released of the Pokemon games")

#20 versions

#Q5 Print out the name of every electric-type pokemon.*****

type_response = requests.get("https://pokeapi.co/api/v2/type/electric")
type = type_response.json()

print (type)
print (type ['pokemon'][0]['pokemon']['name'])

electric_types = type['pokemon']
for electric_type in electric_types:
    print (electric_type['pokemon']['name'])

#Q6 What are electric-type Pokemon called in the Korean version of the game? *****

print (type["names"])
print (type["names"][1])
print (type["names"][1]["name"])

#전기

#Q7 Who has a higher speed stat, Eevee or Pikachu?

#pokemons_response = requests.get('https://pokeapi.co/api/v2/pokemon')

#Eevee's speed
eevee_response = requests.get('https://pokeapi.co/api/v2/pokemon/eevee')
eevee = eevee_response.json()
print (eevee)
print (eevee.keys())
print(eevee['stats'])

for eve in eevee['stats']:
    if eve['stat']['name'] == 'speed':
        print(eve['base_stat'])
        print(eve['stat']['name'])

# speed of Eevee is 55

pikachu_response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
pikachu = pikachu_response.json()
print (pikachu)
print (pikachu.keys())
print(pikachu['stats'])
print(pikachu['stats'][0])
print(pikachu['stats'][0].keys())
print(pikachu['stats'][0]['base_stat'])

for pika in pikachu['stats']:
    if pika['stat']['name'] == 'speed':
        print(pika['base_stat'])
        print(pika['stat']['name'])

# speed of Eevee is 90

if pika['base_stat'] > eve['base_stat']:
    print("Pikachu has the higher speed than Eevee")
elif pika['base_stat'] < eve['base_stat']:
    print("Eevee has the higher speed than Pikashu")
 

