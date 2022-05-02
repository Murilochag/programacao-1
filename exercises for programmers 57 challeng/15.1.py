import getpass
user = input('user: ')
# password = getpass.getpass('what is the password: ')


if user == 'a':
    print('welcome user a')
    password = getpass.getpass('what is the password: ')
    if password == 'a12345' :
     print('\nwelcome!\n')
    else : print("i don't konow you")
elif user == 'b':
    print('welcome user b')
    password = getpass.getpass('what is the password: ')
    if password == 'b12345' :
     print('\nwelcome!\n')
    else : print("i don't konow you")
elif user == 'c':
    print('welcome user c')
    password = getpass.getpass('what is the password: ')
    if password == 'c12345' :
     print('\nwelcome!\n')
    else : print("i don't konow you")
elif user == 'd':
    print('welcome user d')
    password = getpass.getpass('what is the password: ')
    if password == 'd12345' :
     print('\nwelcome!\n')
    else : print("i don't konow you")
else : print('ERRO')

