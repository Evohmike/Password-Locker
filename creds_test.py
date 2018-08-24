import unittest
from creds import Credentials


class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Evoh","Evohmike","evohmike@py.com","12345")
    def test_credentials_init(self):
        '''
        This tests if the object has been initialized properly
        '''
        self.assertEqual(self.new_credentials.account_name, "Evoh")
        self.assertEqual(self.new_credentials.user_name, "Evohmike")
        self.assertEqual(self.new_credentials.email, "evohmike@py.com")
        self.assertEqual(self.new_credentials.password, "12345")

        
if __name__=='__main__':
    unittest.main()