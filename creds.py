

class Credentials:
  '''
  This class generates user credentials
  '''
  credentials_list=[]

  def __init__ (self,account_name,user_name,email,password):
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

    Credentials.Credentials_List.append(self)
