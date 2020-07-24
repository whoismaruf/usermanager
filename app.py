from scripts.user import User

print('Welcome to user management CLI application')

user_list = {}

def create_account():
    name = input('Say your name: ')
    email = input('Enter email: ')
    user = User(name, email)
    uname = user.set_username()
    current_user = {
        'name': name,
        'email': email
    }
    while True:
        if uname in user_list:
            new_uname = input(f'Sorry your username "{uname}" has been taken, choose another one: ')
            uname = new_uname.replace(" ", '')
        else:
            break
    user_list[f'{uname}'] = current_user
    print(f"Hello, {name}! Your account has been created")


while True:
    user_input = input('''
        A --> Create account
        S --> Show account info
        Q --> Quit
    ''')
    if user_input == 'A' or user_input == 'a':
        create_account()
    elif user_input == 'S' or user_input == 's':
        if len(user_list) == 0:
            print("There is no account, please create one")
            continue
        else:
            while True:
                search = input('Enter username: ')
                if search not in user_list:
                    print(f"Your searched '{search}' user not found. Please search again")
                else: 
                    res = user_list[search]
                    print(f'''
                        Account information for {search}
                        Name: {user_list[search]['name']}
                        Email: {user_list[search]['email']}
                    ''')
                    break
    elif user_input == 'Q' or user_input == 'q':
        break
    else:
        print('Bad input, try again')