import requests

ingredient = input("What are we cooking? ")

api_id = '59d44081'
api_key = '9c5d1a87c618ed07d59288d748d5f070'

url = f'https://api.edamam.com/search?q={ingredient}&app_id={api_id}&app_key={api_key}'
response = requests.get(url)
eda_resp = response.json()

hits = eda_resp['hits']

# def run():
#
#     for hit in hits:
#         recipe = hit['recipe']
#
#         print(recipe['label'])
#         print(recipe['url'])
#         print(recipe['ingredientLines'])
#
# run()

with open("recipe_book.txt", "a") as o:
    for hit in hits:
        recipe = hit['recipe']

        o.write(recipe['label'])
        o.write('\n')
        o.write(recipe['url'])
        o.write('\n')
        ingredients = recipe['ingredientLines']
        for ingredient in ingredients:
            o.write(ingredient)
            o.write('\n')
        o.write('\n\n')


