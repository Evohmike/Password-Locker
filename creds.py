
import pyperclip
# import Random

class Credentials:
    '''
    This class generates user credentials
    '''
    credentials_list = []


    def __init__(self, account_name, user_name, email, password):
        '''
        This method defines the properties of the user credentials.
        '''
        self.account_name = account_name
        self.user_name = user_name
        self.email = email
        self.password = password

    def save_credentials(self):
         '''
         This saves credential objects into credential list
         '''
         Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_contact method deletes an object from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list


    @classmethod
    def find_by_user_name(cls, name):
        '''
        This is a method that takes in a user name and returns a credential that matches the name.
        '''
        for credentials in cls.credentials_list:
            if credentials.user_name == name:
                return credentials

    @classmethod
    def credentials_exist(cls, name):
        '''
        Method that check if the credentials are already on tha contact_list
        and return true(if it exists) and false(if it does not)
        '''
        for credentials in cls.credentials_list:
            if credentials.user_name == name:
                return True

        return False
