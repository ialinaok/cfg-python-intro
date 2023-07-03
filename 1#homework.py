# task 1

chairs = '15'
nails = 4

total_nails = chairs * nails

message = 'I need to buy {} nails'.format(total_nails)

print('You need to buy {} nails'.format(message))

# there are two problems:
# - the number of chairs is given as a string - fix by deleting quotations
# - we pass double the sentence to print a message - fix by only putting placeholder in print

chairs = 15
nails = 4

total_nails = chairs * nails

message = 'I need to buy {} nails'.format(total_nails)

print('{}'.format(message))

# task 2

my_name = 'Penelope'
my_age = 29

message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

# the error says: name 'Penelope' is not defined
# the variable value should be in quotations to make it a string

# task 3

how_many_boxes = 2
how_many_eggs = how_many_boxes * 6
eggs_in_omelette = 9
how_many_omelettes = int(how_many_eggs / eggs_in_omelette)

message = 'You can make {} omelettes with {} boxes of eggs'.format(how_many_omelettes, how_many_boxes)
print(message)
