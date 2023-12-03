import requests
import json

ship = ''
request = requests.get('https://swapi.dev/api/starships/')
data = json.loads(request.text)

for i in data['results']:
    if i['name'] == 'Millennium Falcon':
        ship = i

ship_attrs = ['name', 'max_atmosphering_speed', 'starship_class', 'pilots']
ship_miss_attrs = [key for key in ship if key not in ship_attrs]
for i in ship_miss_attrs:
    ship.pop(i)

pilot_attrs = ['name', 'height', 'mass', 'homeworld', 'homeworld_url']
for i in range(len(ship['pilots'])):
    ship['pilots'][i] = json.loads(requests.get(ship['pilots'][i]).text)
    ship['pilots'][i]['homeworld_url'] = ship['pilots'][i]['homeworld']
    ship['pilots'][i]['homeworld'] = (json.loads(requests.get(ship['pilots'][i]['homeworld']).text))['name']
    pilot_miss_attrs = [key for key in ship['pilots'][i] if key not in pilot_attrs]
    for v in pilot_miss_attrs:
        ship['pilots'][i].pop(v)

with open('task1.json', 'w') as file:
    json.dump(ship, file, indent=4)

print(json.dumps(ship, indent=4))