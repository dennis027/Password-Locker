# import pyperclip
class User:
    """generates a class user"""
    user_list = [] # empty user list
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)




    def __init__(self,create_account,login):

        '''
        __init__ method that helps us define properties for our objects.

       '''
        self.create_account = create_account
        self.login = login










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