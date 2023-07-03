import requests

def recipe_search(ingredient):
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = '59d44081'
    app_key = '9c5d1a87c618ed07d59288d748d5f070'
    result = requests.get(
'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

def run():
    ingredient = input('Enter an ingredient: ')

    results = recipe_search(ingredient)

    for result in results:
        recipe = result['recipe']

        print(recipe['label'])
        print(recipe['uri'])
        print()

run()