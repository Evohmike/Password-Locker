import unittest
from creds import Credentials


class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Evoh", "Evohmike", "evohmike@py.com", "12345")

    def tearDown(self):
        '''
        This method cleans up after each test case has run
        '''
        Credentials.credentials_list = []

    def test_credentials_init(self):
        '''
        This tests if the object has been initialized properly
        '''
        self.assertEqual(self.new_credentials.account_name, "Evoh")
        self.assertEqual(self.new_credentials.user_name, "Evohmike")
        self.assertEqual(self.new_credentials.email, "evohmike@py.com")
        self.assertEqual(self.new_credentials.password, "12345")

    def test_save_credentials(self):
        '''
        Test if the credentials objects are saved into the credentials list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        '''
        This checks if we can save multiple credentials objects into the credentials list.
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Peter", "petero", "peter@py.com", "abcdef")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)


if __name__ == '__main__':
    unittest.main()
