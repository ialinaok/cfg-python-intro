import random

first_names = [
    'Jessica',
    'Jacob',
    'Maria',
    'Carl',
    'Maximilian',
    'Bożena',
    'Thymen'
]

last_names = [
    'Bogers',
    'Glaven',
    'Dortmay',
    'Sengros',
    'de la Cruz',
    'Escavian',
    'Hoyos Cortes'
]

first_name = random.choice(first_names)
last_name = random.choice(last_names)

print('{} {}'.format(first_name, last_name))