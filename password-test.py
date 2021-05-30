from typing import ClassVar
import unittest
from password import User
from password import Credentials

class TestUser(unittest.TestCase):
    """
    test class that defines test case of Userclass
    Args
       unittest.TestCase class that help in creating unitest
    """
    def setUp(self):
        """
        setup method helping us run each testcase
        """
        self.new_user = User(True , False)# creates a contact object
        self.new_credentials = Credentials("dennis","bandict123")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        Credentials.credentials_list = []

    def test_init(self):
        """
        test_init method checking if object is initialised properly
        """
        self.assertEqual(self.new_user.create_account,True)
        self.assertEqual(self.new_user.login,False)
        self.assertEqual(self.new_credentials.username, "dennis")
        self.assertEqual(self.new_credentials.password,"bandict123") 



    def test_save_User(self):
        """
        test save user login and create user and if its save in User list
        """  
        self.new_user.save_user()#saves the new user
        self.assertEqual(len(User.user_list),1)

    def test_save_Credentials(self):
        """
        test save credentials and create list  if it saves Credentials
        """
        self.new_credentials.save_credentials()#saves new credentials
        self.assertEqual(len(Credentials.credentials_list),1)


 


    def test_save_credentials(self):
        """
        test_save_multiple_credentials
        to check if we can save multiple credentials
        objects to our credential list
        """  
        self.new_credentials.save_credentials()
        test_credentials = Credentials ("kimani","mee")   #new credentials .save
        self.assertEqual (len(Credentials.credentials_list),1)

    def test_delete_credentials(self):
        """
        test if we can remove a credential from our application
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials ("kimani","mee")#new account user_list
        self.new_credentials.delete_credentials()#delete credential
        self.assertEqual(len(Credentials.credentials_list),0)


    def test_find_credentials_by_name(self):
        """
        test to test_find_credentials_by_name and display information
        """ 
        self.new_credentials.save_credentials()
        test_credentials = Credentials("kimani","mee") #new credentials_list
        test_credentials.save_credentials()
        found_credentials = Credentials("kimani")
        self.assertEquals(found_credentials,found_credentials.password,test_credentials.password)


if __name__ == '__main__':
    unittest.main()  


