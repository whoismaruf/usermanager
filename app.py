from scripts.user import User

print('\nWelcome to user management CLI application')

user_list = {}

def create_account():
    
    name = input('\nSay your name: ')

    while True:
        email = input('\nEnter email: ')
        if '@' in email:
            temp = [i for i in email[email.find('@'):]]
            if '.' in temp:
                user = User(name, email)
                break
            else:
                print("\nInvalid Email address! Please enter the correct one.")
                continue
        else:
            print("\nInvalid Email address! Please enter the correct one.")
            continue
    
    uname = user.set_username()

    current_user = {
        'name': name,
        'email': email
    }

    while True:
        if uname in user_list:
            new_uname = input(f'\nSorry your username "{uname}" has been taken, choose another one: ')
            uname = new_uname.replace(" ", '')
        else:
            break
    
    user_list[f'{uname}'] = current_user
    print(f"\nHello, {name}! Your account has been created as {uname}.\n\nChoose what to do next - ")


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
            print("\nThere is no account, please create one")
            continue
        else:
            while True:
                search = input('\nEnter username: ')
                if search not in user_list:
                    print(f"\nYour searched '{search}' user not found.")
                    pop = input('''
                        S --> Search again
                        M --> Back to main menu
                    ''')
                    if pop == 'S' or pop == 's':
                        continue
                    elif pop == 'M' or pop == 'm':
                        break
                    else:
                        print('Bad input')
                        break
                else: 
                    res = user_list[search]
                    print(f'''

                        Account information for {search}
                        Name: {res['name']}
                        Email: {res['email']}

                    ''')
                    break
    elif user_input == 'Q' or user_input == 'q':
        break
    elif user_input == '':
        print('Please input something')
        continue
    else:
        print('\nBad input, try again\n')