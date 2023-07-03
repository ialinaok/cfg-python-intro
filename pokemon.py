import requests

pokemon_number = input("What is the Pokemon ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)

pokemon = response.json()

print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])

# let's us make http requests to get information from websites