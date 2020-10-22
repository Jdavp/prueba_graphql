import requests
import json
import os
from time import sleep

film_dict = {}
characters = {}
planet_dict = {}
film_index = 1
planet_index = 1
character_index = 1

# request to get all the requery data
for i in range(10):
    sleep(0.1)
    page_index = i+1
    r = requests.get(f'https://swapi.dev/api/people/?page={page_index}')
    response = r.json()
    if 'results' in response:
        for person in response['results']:
            films_urls = person['films']
            films = []

            for film_url in films_urls:
                if film_url in film_dict:
                    film = film_dict[film_url]
                else:
                    sleep(0.1)
                    r2 = requests.get(film_url)
                    response2 = r2.json()
                    film_title = response2['title']
                    opening_crawl = response2['opening_crawl']
                    director = response2['director']
                    producer = response2['producer']
                    planets = []

                    for planet in response2['planets']:
                        sleep(0.1)
                        r3 = requests.get(planet)
                        response3 = r3.json()
                        planet_name = response3['name']
                        if planet_name in planet_dict:
                            planets.append(planet_dict[planet_name])
                        else:
                            planet_dict[planet_name] = {'pk': planet_index, 'name': planet_name}
                            planets.append(planet_dict[planet_name])
                            planet_index = planet_index+1
                        print(planet_name)
                    film = {
                        'film_title': film_title,
                        'opening_crawl': opening_crawl,
                        'director': director,
                        'producer': producer,
                        'planets': planets,
                        'film_id': film_index
                    }
                    film_index = film_index+1
                    film_dict[film_url] = film
                films.append(film)
            characters[character_index] = {
                'pk': character_index,
                'name': person['name'],
                'films': films
            }
            character_index = character_index+1

model = []
# shape json for the requirements as model request in fixture  
for planet_name in planet_dict:
    model.append({
        'model':'characters.planet',
        'pk': planet_dict[planet_name]['pk'],
        'fields': {
            'name': planet_name
        }
    })

for film_url in film_dict:
    model.append({
        'model':'characters.film',
        'pk': film_dict[film_url]['film_id'],
        'fields': {
            'film_title': film_dict[film_url]['film_title'],
            'director': film_dict[film_url]['director'],
            'producer' : film_dict[film_url]['producer'],
            'opening_crawl' : film_dict[film_url]['opening_crawl'],
            'planets' : [x['pk'] for x in film_dict[film_url]['planets']]
        }
    })

print(characters)
for character_id in characters:
    model.append(
        {
            'model':'characters.character',
            'pk': character_id,
            'fields':{
                'name': characters[character_id]['name'],
                'films': [x['film_id'] for x in characters[character_id]['films']]
            }
        }
    )
os.chdir(r'characters/fixtures/')
with open('starwars.json', 'w') as jsonfile:
    json.dump(model, jsonfile)
