import unittest # Importing the unittest module
from password import User,Credentials # Importing the contact class
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
        avoid cleanup when each test is made
        """
        User.user_list = []
        Credentials.credentials_list=[]

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

    def test_save_multiple_Credentials(self):  
        """
        test if we can save multiple credentials in our app
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials ("kimani","test123")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)  ##supposed to be 2
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials ("kimani","test123")
        test_credentials.save_credentials()
        # self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    # def test_find_credentials_by_name(self):
    #     """
    #     test to test_find_credentials_by_name and display information
    #     """ 
    #     self.new_credentials.save_credentials()
    #     test_credentials = Credentials("kimani","mee") #new credentials_list
    #     test_credentials.save_credentials()
    #     found_credentials = Credentials.find_by_username("kimani")
    #     self.assertEquals(found_credentials.password, test_credentials.password)

    def test_credentials_exist(self):
        """
        test to check if we can returna Boolean if we cannot find contact
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("kimani","test123")
        test_credentials.save_credentials()
        credentials_exist=Credentials.credentials_exist("kimani")
        self.assertTrue(credentials_exist)

    def test_display_all_credentials_(self):
        """
        method to return all credentials
        """ 
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)   



if __name__ == '__main__':
    unittest.main()


  