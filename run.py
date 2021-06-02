#!/usr/bin/env python3.6
from password import User,Credentials
from random import *



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


def response_none(question):
    """Users response on whether to generate password or not"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def main():
    print("****************")
    print('\n')
    print(f"Welcome to Pass Lock,helping you save and remember your passwords is our priority.")
    print('\n')
    print("****************")
    print('\n')
    print("Please create Account:")
    print('\n')

    print("Enter your new username")
    username = input()
    print("Enter your new password")
    password = input()
    save_user(create_user(username, password))
    print('\n')
    

    print("****************")
    print('\n')
    print(f"Hello {username}, Thank you for creating an account with us.")
    print('\n')
    print("****************")

    print("Login")
    print('\n')

    print("Enter your username:")
    username = input()

    print("Enter your password:")
    password = input()
    print('\n')

  
# def copy_password():
#     '''
#     function that copies the password
#     '''  
#     return Credentials.copy_password()         

###main function


def main(): 

  
    # user_name = input()
    # print(f"hello {user_name} what would you like to do")
    # print("\n")

    while True:
        print("use these short codes cc to create credentials,dc to display credentials and fc to find credentials,gb for goodbyee")
        print("\n")
        short_code=input().lower()
        if short_code=='cc':
            print("New Credentials")
            print("-"*10) 
            print("username=......")  
            username=input()
            print("password=......") 
            generate = response_none(
            #check if user want to be given a new password
            if generate =="y":
                characters = string.ascii_letters + string.punctuation  + string.digits
                password =  "".join(choice(characters) for x in range(randint(8, 16)))
                print password
            else:    


            password=input()

            save_credentials(create_credentials(username,password))#creates and saves new username and copy_password
            print('\n')
            print(f"New Credentials {username} {password} was created")
            print('\n')
            print(f"New Credentials {username} {password} was created")
            print('\n')
        elif short_code == "dc":
            if display_credentials():
                print("here is your list of credentials")
                print('\n')
                for credentials in display_credentials():
                    print(f"{credentials.username}:{credentials.password}")
                    print('\n')
                else:
                    print("your credentials list is empty")

        elif short_code == "fc":
            print("enter the username you want to search for password")
            search_username=input()
            if check_existing_credentials(search_username):
                search_credential =find_credentials(search_username)
                print(f"search_credential.username")
                print('-' *20)
                print(f"your password for the credential is{search_credential.password}")
            else:
                print("that does not exist")
        elif short_code == "gb":
            print("byeeee..........")  
            break
        else:
             ("i really didnt get that prease repeat yourself")      




if __name__ == '__main__':
    main()

