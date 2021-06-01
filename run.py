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

    print("Hello, welcome to the password keeper app are you a new user whats your name? ")
    # if print==("yes"):
    #     print("imput username")
    #     print("imput password")
    #     elif ==("no")
    #     print("imput username")
    #     print("imput password")
    user_name = input()
    print(f"hello {user_name} what would you like to do")
    print("\n")

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
                    print("your contact list is empty")

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

