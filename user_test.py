
#!usr/bin/env python3.9
import unittest #import unittestmodule
from user import User #import the user class
class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test
        '''
        self.new_user=User("EsauKip","#Youcannotfind5") #new User created
    def test__init(self):
       
        self.assertEqual(self.new_user.username,"EsauKip")
        self.assertEqual(self.new_user.password,"#Youcannotfind5")
        ##second test
    def test_save_user(self):
        '''
        check whether the user information can be saved 
        in the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        User.user_list = []
        #save many users
    def test_save_multiple_users(self):
       self.new_user.save_user()
       test_user = User("test","trickysana")
       test_user.save_user()
       self.assertEqual(len(User.user_list),2)
       #4th test
    def test_delete_user(self):
        '''
        check whether one can delete a user account
        '''
        self.new_user.save_user()
        test_user = User("try", "trickysana")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)
        #5th test
    def test_find_user(self):
        '''
        find a user using username
        '''
        self.new_user.save_user()
        test_user = User("try", "trickysana")
        test_user.save_user()
        found_user = User.find_user("EsauKip")
        self.assertEqual(found_user.username, self.new_user.username)
if __name__ == "__main__":
    unittest.main()
@classmethod
def contact_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                    return True

        return False