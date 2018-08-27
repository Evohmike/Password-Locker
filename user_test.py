import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        method run before each test case
        '''
        self.new_user = User("Reagandisi", "paswad")


    def tearDown(self):
        '''
        Method to give an empty array before each test for more accurate results
        '''
        User.user_list = []
    def test_user_init(self):
        '''
        method to test if our users are being instantiated correctly
        '''
        self.assertEqual(self.new_user.login_name, "Reagandisi")
        self.assertEqual(self.new_user.password, "paswad")



    def test_save_user(self):
        '''
        Method to test if users are being saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


    def test_save_multiple_user(self):
        '''
        Method to test if multiple users are being saved
        '''
        self.new_user.save_user()
        test_user = User("sharon", "passd")
        test_user.save_user()

        self.assertEqual(len(User.user_list), 2)

    def test_login(self):
        '''
        method to test login credentialss
        '''
        self.new_user.save_user()
        test_user = User("mike_onyango", "password")
        test_user.save_user()

        login_credentials = User.user_login("mike_onyango")
        self.assertEqual(login_credentials.login_name, test_user.login_name)


if __name__ == '__main__':
    unittest.main(verbosity=2)
