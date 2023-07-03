fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2 },
    {'name': 'pear', 'colour': 'green', 'price': 0.19}
]

for fruit in fruits:
    print(fruit['name'])
    print(fruit['colour'])
    print(fruit['price'])
    print('{} {} {}'.format(fruit['name'], fruit['colour'], fruit['price']))