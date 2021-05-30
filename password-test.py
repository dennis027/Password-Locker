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
    def test_init(self):
        """
        test_init method checking if object is initialised properly
        """
        self.assertEqual(self.new_user.create_account,True)
        self.assertEqual(self.new_user.login,False)
if __name__ == '__main__':
    unittest.main()        
