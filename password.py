class User:
    "generate a class for the users"
    def __init__(self, create_account,login):
        self.name = create_account
        self.login = login



class Credentials:
    "generates a class for the credentials"
    def __init__(self,username,password):
        self.username = username
        self.password = password