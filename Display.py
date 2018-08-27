#!/usr/bin/env python3.6

from creds import Credentials
from user import User

def create_account(username,password):
  '''
  This function creates new account
  '''
  new_user = User(username,password)
  return new_user

def save_new_user(user):
  '''
  This function saves a user
  '''
  User.save_user(user)

def login_account(login):
  return User.user_login(login)

def create_credentials(account,username,email,password):
  '''
  This creates new credentials
  '''
  new_credentials = Credentials(account,username,email,password)
  return new_credentials

def save_user_credentials(credentials):
  '''
  This function saves credentials
  '''
  credentials.save_credentials()

def delete_credentials(credentials):
  '''
  This deletes credentials
  '''
  credentials.delete_credentials()

def find_credentials(name):
  '''
  this finds the credentials using account name and returns details
  '''
  return Credentials.find_by_account_name(name)

def copy_username(name):
    return Credentials.copy_username(name)

def check_credentials_exist(name):
    '''
    This function to check if a credentials exists
    '''
    return Credentials.credentials_exist(name)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def generate_password(password_length):
    return Credentials.generate_password(password_length)


def main():
    print("HELLO! WELCOME TO PASSWORD LOCKER!!")
    while True:
        print('''
              ca - create account
              log - login
              esc - Escape''')
        short_code = input().lower()
        if short_code == "ca":
            print("Create Acount")
            print("First, Create a username:")
            print("_" * 20)
            username = input()
            password= input("Choose a password of your choice: ")
            print("_" * 20)
            save_new_user(create_account(username, password))
            print(f"""Your user details - Username : {username} Password : {password}""")
            print("")
            print(f"Hello {username} Choose the options below")
            print("")

            while True:
                print("Use these short codes: cc - create new credentials, dc - display credentials,  fc - find a credentials, wq - exit credentials list")
                short_code = input().lower()

                if short_code == 'cc':
                        print("New credentials")
                        print("-"*40)

                        print('')

                        print("Account name ...")
                        a_name = input()

                        print('')

                        print("User name ...")
                        u_name = input()

                        print('')

                        print("Email address ...")
                        email = input()

                        print('')

                        print("Account password")
                        acc_password = input()
                        print('')

                        save_user_credentials(create_credentials(a_name, u_name, email, acc_password))
                        print('')

                        print(f"New credential account : {a_name}, User name : {u_name}")
                        print('')

                elif short_code == 'dc':
                        if display_credentials():
                            print("This is a list of all the credentials")
                            print('')
                            for Credentials in display_credentials():
                                print(f"Account : {Credentials.account_name}, User name : {Credentials.user_name} E-mail address : {Credentials.email} Password : {Credentials.password}")

                                print('')
                        else:
                            print('')
                            print("I'm sorry, you seem not to have saved any credentials")
                            print('')
                elif short_code == 'fc':
                        print("Enter the Account you want")
                        search_name = input()
                        if check_credentials_exist(search_name):
                                search_name = find_credentials(search_name)
                                print('')
                                print(f"{search_name.user_name} {search_name.email}")
                                print('-'*20)

                                print('')

                                print(f"Account ... {search_name.account_name}")
                                print(f"Password ... {search_name.password}")
                                print('')

                        else:
                                print('')
                                print("Credentials do not exist")
                                print('')
               

                elif short_code == "wq":
                        print('')
                        print("Goodbye ...")
                        break
                else:
                    print("Please input a valid  code")

        elif short_code == "log":
            print("Log in")
            print("Enter User Name")
            uname = input()
            print("Enter password")
            password = input()
            print("_" * 20)

            print(f"Hello {uname} Kindly choose the options below")
            print("")
            while True:
                print("Use these short codes: cc - create new credentials, dc - display credentials, wq - exit credentials list")
                short_code = input().lower()

                if short_code == 'cc':
                        print("New credentials")
                        print("-"*10)

                        print('')

                        print("Account name ...")
                        a_name = input()

                        print('')

                        print("User name ...")
                        u_name = input()


            print(f"Hello {uname} Kindly choose the options below")
            print("")
            while True:
                print("Use these short codes: cc - create new credentials, dc - display credentials, wq - exit credentials list")
                short_code = input().lower()

                if short_code == 'cc':
                        print("New credentials")
                        print("-"*10)

                        print('')

                        print("Account name ...")
                        a_name = input()

                        print('')

                        print("User name ...")
                        u_name = input()

                        print('')

                        print("Email address ...")
                        email = input()

                        print('')

                        print("Account password")
                        acc_password = input()

                        save_user_credentials(create_credentials(a_name, u_name, email, acc_password))
                        print('')

                        print(f"New credential account : {a_name}, User name : {u_name}")
                        print('')
                elif short_code == 'dc':
                        if display_credentials():
                            print("This is a list of all the credentials")
                            print('')
                            for Credentials in display_credentials():
                                print(f"Account : {Credentials.account_name}, User name : {Credentials.user_name} E-mail address : {Credentials.email} Password : {Credentials.password}")

                                print('')
                        else:
                            print('')
                            print("I'm sorry, you seem not to have saved any credentials")
                            print('')
             
                elif short_code == "wq":
                        print('')
                        print("Goodbye ...")
                        break
                else:
                    print("Please input a valid  code")

        elif short_code == "esc":
            print('')
            print("Exiting")
            break
        else:
            print("The short code does not seem to exist,please try again")




if __name__ == '__main__':

    main()