import random

bet = input('How much do you bet? ')
usr_colour = input('What color do you pick, red or black? r/b ')
usr_number = int(input('Pick a number between 1 and 100: '))


def colour():
    random_nbr = random.randint(1, 2)
    if random_nbr == 1:
        colour = 'r'
    else:
        colour = 'b'
    return colour


random_number = random.randint(1, 100)
random_colour = colour()
print('random colour: {} \nrandom number: {}'.format(random_colour, random_number))

if random_colour == usr_colour:
    print('You keep your bet \n{}'.format(bet))
elif random_number == usr_number:
    bet = 2 * bet
    print('You win double the amount you bet! \n{}'.format(bet))
elif random_colour == usr_colour and random_number == usr_number:
    bet = 100 * bet
    print('OMG, you win 100 times what you bet! \n{}'.format(bet))
else:
    bet = 0
    print('Sorry, you win nothing... \n{}'.format(bet))
