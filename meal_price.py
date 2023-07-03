meal_price = float(input('How much did the meal cost? '))

discount_choice = input('Do you have a discount? y/n ')
discount_applicable = discount_choice == 'y'

if discount_applicable and meal_price > 20.00:
    total_price = meal_price - 0.1 * meal_price
    print('Discount applied. You should pay {}euros'.format(total_price))

else:
    print('No discount applied. You should pay {} euros'.format(meal_price))