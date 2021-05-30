class User:
    "generate a class for the users"
    user_list = []  #user list
    def save_user(self):
        """
        saves new user credentials into contact list
        """
        User.user_list.append(self)
    def __init__(self, create_account,login):
        """
        helping us define properties of our users
        """
        self.create_account = create_account
        self.login = login



class Credentials:
    "generates a class for the credentials"
    credentials_list = [] #credentials list
    def save_credentials(self):
        """
        saves new user credentilas into contact user_list
        """
        Credentials.credentials_list.append(self)
    def __init__(self,username,password):
        """
        helping us denine proprert of our credentials
        """
        self.username = username
        self.password = password