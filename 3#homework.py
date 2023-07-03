
# Q1

# is_raining = input("is it raining outside? y/n ")
#
# if is_raining == 'y':
#     print("Better take an umbrella!")
# if is_raining == 'n':
#     print("you don't need an umbrella, enjoy the weather ˆˆ")

# Q2
#
# my_money = int(input("how much money do you have? "))
# boat_cost = 20 + 5
#
# if my_money > boat_cost:
#     print("You can afford the boat hire")
# else:
#     print("You cannot afford the boat hire")

# - boat cost written wrong
# - comparison sign should be the opposite
# - conversion of input to integer was missing

# Q3

year = int(input("when was the book written? "))
century = int(year / 100)
decade = int((year - century * 100)/10) * 10

print("{}th century, {}'s".format(century, decade))