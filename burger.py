burgerprice = float(input("What's the price of the burger? "))
veggie = input('"Does the restaurant have veggie option? y/n ')

has_veggie = veggie == 'y'
within_budget = burgerprice <= 10.00

meets_criteria = within_budget and has_veggie

if meets_criteria:
    print("This restaurant is a great choice!")

if not meets_criteria:
    print("Probably not a good idea...")
