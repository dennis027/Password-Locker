# import pyperclip
class User:
    """generates a class user"""
    user_list = [] # empty user list
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_user_details(self):
        """
        save_contact method saves contact objects into user_array
        """
        User.users_array.append(self)

    @classmethod
    def display_users(cls):
        """
        method that returns the class array
        """
        return cls.users_array


class Credential:
    """
    a class that generates new credential for users
    """
    pass
    credential_array = []

    def __init__(self, user_name, password, email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_credential(self):
        """
        save_contact method saves credentials objects into credential_array
        """
        Credential.credential_array.append(self)

    @classmethod
    def display_credential(cls):
        """
        method that returns the credential array
        """
        return cls.credential_array









class Credentials:
    """this generates password credentials"""    
   

    credentials_list = [] #empty list of credentials
    def save_credentials(self):

        '''
        save_credentials method saves credential objects into credntial_list
        '''

        Credentials.credentials_list.append(self)
    

        '''
        __init__ method that helps us define properties for our objects.

        '''
    def delete_credential(self):
        """
        delete_credentials saved from credentials list
        """ 
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_username(cls, username):
        """
        method takes a username and returns password
        """
        for credentials in cls.credentials_list: 
            if credentials.username == username:
                return credentials.password  

    @classmethod
    def credentials_exist(cls, username):
        """
        method that check if a contact exist from thr credentials list
        """ 
        for credentials in cls.credentials_list: 
            if credentials.username == username:
                return True

    @classmethod
    def display_credentials(cls):
        """
        method returning the credentials list
        """ 
        return cls.credentials_list    

    # @classmethod
    #     def copy_password(cls, password):
    #         credentials_found = Credentials.find_by_username(username)
    #         pyperclip.copy(credentials_found, password)                       

    def __init__(self,username,password):    
        self.username = username
        self.password = password