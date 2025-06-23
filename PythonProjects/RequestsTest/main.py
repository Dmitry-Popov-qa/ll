import requests

URL ='https://api.pokemonbattle.ru/v2'
TOKEN ='142ad3e830b44bec3b7acf51d84683ab'
HEADER ={'Content-Type' : 'application/json','trainer_token' :TOKEN}

body_create = {
    "name": "Бульбббазавр",
    "photo_id": '12'
} 

body_create = {
    "pokemon_id": "342317",
    "name": "BOB",
    "photo_id": '2'
}
body_create = {
    "pokemon_id": "342317"
}

'''response_create= requests.post(url=f'{URL}/pokemons',headers=HEADER,json=body_create)
print (response_create.text)'''

'''response_create= requests.put(url=f'{URL}/pokemons',headers=HEADER,json=body_create)
print (response_create.text)'''

response_create= requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER,json=body_create)
print (response_create.text)