from scripts.user import User
import sqlite3

print('Welcome to user management CLI application')

name = input('Say your name: ')
email = input('Enter email: ')


user = User(name, email)
uname = user.set_username()

current_user = {
    'name': name,
    'email': email
}

user_list = {}
user_list[f'{uname}'] = current_user

print(user_list)