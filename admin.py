name = input("what is your name? ")
is_admin = name == 'admin'

password = input('What\'s your password? ')
is_password_correct = password == 'dinosaurs'

if is_admin and is_password_correct:
    print('Welcome')

if not is_admin or not is_password_correct:
    print('Go away')