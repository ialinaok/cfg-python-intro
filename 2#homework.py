# Q1

for number in range(100):
    output = 'o' * number
    print(output)

# so the program outputs a certain amount of letters 'o'
# in the for loop, the number value is going to increase every
# time the loop iterates - and since we print out the 'o' times
# number * 'o', every time there will be a new call to print
# it'll print a new amount of 'o's

# Q2

def calculate_vat(amount):
    amount = amount * 1.2
    return amount

total = calculate_vat(100)
print(total)

# Q3
# seriously
