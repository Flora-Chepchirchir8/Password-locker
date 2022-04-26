# import pyperclip
class Credentials:
    '''generate instance of Credentials class
    '''
    credentials_list = []
    # assign property to credential list
    def __init__(self,account,email,password):
        self.account = account
        self.email = email
        self.password = password
    def save_credentials(self):
        '''
        self credentials in credential_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete credentials 
        '''
        Credentials.credentials_list.remove(self) 
            # create credentials
    def create_credentials(account, email, password):
        '''
        method credentials details
        '''
        new_credentials = Credentials(account, email, password)
        return new_credentials
    @classmethod
    def find_account(cls, account):
        '''
        search for accounts
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials    
    @classmethod
    def credentials_exists(cls, account):
        '''
        confirm a class actually exists
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return True
        return False  
        #Display credentials
    @classmethod
    def display_credentials(cls):
        '''
        method that returns all credentials
        '''
        return cls.credentials_list
  
