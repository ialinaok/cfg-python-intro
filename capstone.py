import requests


# check if input is a string
def check_ingredient():
    while True:
        ingredient = input('Please provide the name of the ingredient \n')
        if ingredient.isalpha():
            return ingredient
        print("Sorry!This is not a valid response")


# check if input is in the allowed values range
def check_sort_order():
    while True:
        sort_order = input("Would you like to sort the results by NAME or CALORIES \n")
        if sort_order.lower() in ['name', 'calories']:
            return sort_order
        print("Sorry! This is not a valid input! Please choose NAME or CALORIES")


def check_diet_constr():
    while True:
        diet_constr = input("Do you have any specific diet constrains? \nv - vegan\ngf - gluten-free\nn - none\n")
        if diet_constr in ['v', 'n', 'gf']:
            if diet_constr == 'n':
                return diet_constr
            more_constr = input("Do you have more diet constraints? y/n ")
            if more_constr == 'y':
                diet_constr = diet_constr + ' ' + (input("Please mention other food constraint: \nv - vegan\ngf - gluten-free\n"))
            print(diet_constr)
            return diet_constr
        print("Sorry! We only check for above mentioned constraints!")


# assign the output of functions to a variable
ingredient_choice = check_ingredient()
sort_key = check_sort_order()
diet_choice = check_diet_constr().split()


# retrieve recipe info from the API
def edamam_api_query():
    api_id = '59d44081'
    api_key = '9c5d1a87c618ed07d59288d748d5f070'

    url = f'https://api.edamam.com/search?q={ingredient_choice}&app_id={api_id}&app_key={api_key}'
    response = requests.get(url)
    data = response.json()

    recipes_to_display = []

    for item in data['hits']:
        name = item['recipe']['label']
        ingredients = item['recipe']['ingredientLines']
        calories = round(item['recipe']['calories'], 2)
        added_sugars = round(item['recipe']['digest'][1]['sub'][3]['total'], 2)
        sat_fat = round(item['recipe']['totalNutrients']['FASAT']['quantity'], 2)
        link = item['recipe']['url']
        diet_type = item['recipe']['healthLabels'][0]

        recipe_info = {'name': name, 'calories': calories, 'added sugars': added_sugars, 'saturated fat': sat_fat,
                       'ingredients': ingredients, 'link': link, 'diet type': diet_type}

        if 'v' and 'n' in diet_choice:
            if recipe_info['diet type'].lower() in ['vegan']:
                recipes_to_display.append(recipe_info)
        elif 'gf' and 'n' in diet_choice:
            if recipe_info['diet type'].lower() in ['gluten-free']:
                recipes_to_display.append(recipe_info)
        elif 'v' and 'gf' in diet_choice:
            if recipe_info['diet type'].lower() in ['vegan'] and ['gluten-free']:
                recipes_to_display.append(recipe_info)
        elif 'n' in diet_choice:
            recipes_to_display.append(recipe_info)

        recipes_to_display = sorted(recipes_to_display, key=lambda recipe: recipe[sort_key])

    return recipes_to_display


# save output to a text file
def save_query_output(recipes):
    data_to_write = ""
    for index, recipe in enumerate(recipes):
        with open('recipes.txt', 'w') as recipe_log:
            title_line = ingredient_choice.upper().center(100, '-')
            recipe_log.write(title_line)

        with open('recipes.txt', 'w', encoding='utf-8') as recipe_log:
            data_to_write += '\n' + str(index + 1) + '\n' + 'recipe name:' + recipe['name'] + '\n' + 'calories: ' + str(
                recipe['calories']) + '\n' + 'main ingredients: ' + ','.join(
                recipe['ingredients']) + '\n' + 'link: ' + \
                             recipe['link'] + '\n' + 'diet type:' + recipe['diet type'] + '\n\n'
            recipe_log.write(data_to_write)


recipes = edamam_api_query()
save_query_output(recipes)

# open the file to check contents
with open('recipes.txt', 'r+') as file:
    contents = file.read()
    print(contents)

# ask about: allergies, meal (only show selected), cuisineType;  if nothing - show all
# add 2-3 additional questions w validations, add the data to recipe info, add logic to decide what to display
# based on user responses
