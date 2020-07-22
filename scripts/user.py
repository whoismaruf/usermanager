class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def set_username(self):
        username = self.name.replace(" ", '')
        return username.lower()