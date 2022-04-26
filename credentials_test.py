 #!usr/bin/env python3.9
 import unittest#import unittest module
 from credentials import Credentials
 # import pyperclip
 class TestCredentials(unittest.TestCase):
#     def setUp(self):
#         self.new_credentials = Credentials("Gmail", "florachirry80@gmail.com", "florachirry8")
# #6th test
#     def test_init(self):
#         '''
#         check if instances initialize as expected
#         '''
#         self.assertEqual(self.new_credentials.account, "Gmail")
#         self.assertEqual(self.new_credentials.email, "florachirry80@gmail.com")
#         self.assertEqual(self.new_credentials.password, "florachirry8")
#         #7th test
#     def test_save_credentials(self):
#         '''
#         check if credentials can be saved
#         '''  
#         self.new_credentials.save_credentials()
#         self.assertEqual(len(Credentials.credentials_list),1)
# #save multiple credentials
#     def test_saving_multiple_credentials(self):
#         '''
#         check if users can store multiple credentials
#         '''
#         self.new_credentials.save_credentials()
#         test_credentials = Credentials("Twitter", "trythis","password")
#         test_credentials.save_credentials()
#         self.assertEqual(len(Credentials.credentials_list),2)
#     def tearDown(self):
#         '''
#         clear list before any test is run
#         '''
#         Credentials.credentials_list = []
# #delete credentials 
#     def test_delete_credentials(self):
#         '''
#         test if you can delete credentials test
#         '''
#         self.new_credentials.save_credentials()
#         test_credentials = Credentials("Twitter", "trythis","password")
#         test_credentials.save_credentials()
#         self.new_credentials.delete_credentials()
#         self.assertEqual(len(Credentials.credentials_list), 1)
#         # find credentials 
#     def test_search_for_credentials(self):
#         '''
#         test if credentials can be searched for
#         '''
#         self.new_credentials.save_credentials()
#         test_credentials = Credentials("Twitter", "trythis","password")
#         test_credentials.save_credentials()
#         find_credentials= Credentials.find_account("Twitter")
#         self.assertEqual(find_credentials.account, test_credentials.account)
# # ##credentials check
#     def test_confirm_credentials_exists(self):
#         '''
#         confirm that credentials actually exists
#         '''
#         self.new_credentials.save_credentials()
#         test_credentials = Credentials("Twitter", "trythis","password")
#         test_credentials.save_credentials()
#         credentials_exists = Credentials.credentials_exists("Twitter")
#         self.assertTrue(credentials_exists)
# ##displaying the credentials
     
#     def test_display_credentials(self):
#         '''
#         test if all credentials can be displayed
#         '''
#         self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)
        
      


# if __name__ == "__main__":
#     unittest.main()