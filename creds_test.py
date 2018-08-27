import unittest
import pyperclip
from creds import Credentials


class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials= Credentials("Evoh", "Evohmike", "evohmike@py.com", "12345")

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
        Test if the credentials objects are saved into the credential list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        '''
		This checks if we can save multiple credentials objects into the credentials list.
		'''
        self.new_credentials.save_credentials()
		test_credentials= Credentials("peter", "petero", "peter@py.com", "abcdef")
		test_credentials.save_credentials()
		self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
		'''
		Tests if we can remove credential from Credentials list
	    '''
	    self.new_credentials.save_credentials()
		test_credential= Credentials("peter", "petero", "peter@py.com", "abcdef")
		test_credentials.save_credentials
		self.assertEqual(len(Credentials.credentials_list), 1)

    
    def test_find_credentials_by_user_name(self):
        '''
        This will check if we can find a credentila by user name and display
        information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("omondi", "omosh", "omosh@gmail", "mosh12")
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_user_name("omosh")

        self.assertEqual(found_credentials.email, test_credentials.email

    
    def test_credentials_exist(self):
        '''
         this checks if a credentials exist and return a boolean
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("omondi", "omosh", "omosh@gmail", "omosh12")
        test_credentials.save_credentials()

        credentials_exist = Credentials.credentials_exist
        self.assertTrue(credentials_exist)


    def test_display_all_credentials(self):
        '''
        test method that returns a list of all the credentials saved.
        '''

        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)


    def test_copy_account(self):
        '''
        Test to confirm that we are copying account credentials found
        '''

        self.new_credentials.save_credentials()
        Credentials.copy_username("Max")

        self.assertEqual(self.new_credentials.account_name, pyperclip.paste())

if __name__ == '__main__':
    unittest.main()
