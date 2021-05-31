#!/usr/bin/env python3.6
from password import User,Credentials

def create_user(create_account,login):
    '''
    function to determine user
    '''
    new_user = User(create_account,login)
    return new_user

def save_user(user):
    '''
    function to save the user
    '''  
    user.save_user()  

def create_credentials(username,password):
    '''
    function to create new credentials
    ''' 
    new_credentials= Credentials(username,password)
    return new_credentials   
def save_credentials(credentials):
    '''
    function to save the user
    '''  
    credentials.save_credentials()      

def del_credentials(credentials):
    '''
    Function to delete_credentials
    ''' 
    credentials.delete_credentials() 
def check_existing_credentials(username):  
    '''
    Function that check if a contact exists and returns a boolean
    ''' 
    return Credentials.credentials_exist(username)

def display_credentials(): 
    '''
    Function that returns all the saved credentials
    ''' 
    return Credentials.display_credentials()
# def copy_password():
#     '''
#     function that copies the password
#     '''  
#     return Credentials.copy_password()         

###main function


def main(): 

