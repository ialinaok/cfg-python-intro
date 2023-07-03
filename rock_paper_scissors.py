import random


def random_choice():
    choice_number = random.randint(1, 3)
    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'scissors'
    else:
        choice = 'paper'
    return choice


my_choice = input('Choose rock, scissors or paper: ')
opponent_choice = random_choice()

print('Your opponent chose {}'.format(opponent_choice))

if my_choice == 'rock' and opponent_choice == 'scissors':
    print('You win!')
elif my_choice == 'rock' and opponent_choice == 'paper':
    print('You lose :(')
elif my_choice == 'rock' and opponent_choice == 'rock':
    print('It\'s a tie')
elif my_choice == 'scissors' and opponent_choice == 'scissors':
    print('It\'s a tie')
elif my_choice == 'scissors' and opponent_choice == 'paper':
    print('You win!')
elif my_choice == 'scissors' and opponent_choice == 'rock':
    print('You lose :(')
elif my_choice == 'paper' and opponent_choice == 'paper':
    print('It\'s a tie')
elif my_choice == 'paper' and opponent_choice == 'scissors':
    print('You lose :(')
elif my_choice == 'paper' and opponent_choice == 'rock':
    print('You win ^^')
