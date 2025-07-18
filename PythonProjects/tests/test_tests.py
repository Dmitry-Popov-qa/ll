import requests
import pytest

URL ='https://api.pokemonbattle.ru/v2'
TOKEN ='142ad3e830b44bec3b7acf51d84683ab'
HEADER ={'Content-Type' : 'application/json','trainer_token' :TOKEN}
TRAINER_ID= '36364'

def test_status_code ():
    response = requests.get(url=f'{URL}/trainers',params={'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
   response_get = requests.get(url=f'{URL}/trainers',params={'trainer_id' : TRAINER_ID})
   print  (response_get.json())
   data = response_get.json()['data']
   assert data[0]['trainer_name'] == 'Дмитрий' 

@pytest.mark.parametrize('key,value',[('name', 'nacli'), ('trainer_id',TRAINER_ID), ('id', '342527')])
def test_parametrize(key,value) :
 response_parametrize = requests.get(url=f'{URL}/pokemons',params={'trainer_id' : TRAINER_ID})
 assert response_parametrize.json()['data'][0][key] == value
