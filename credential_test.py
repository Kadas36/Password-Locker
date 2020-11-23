import unittest
import user
from credential import Credential


class TestUser(unittest.TestCase):
    '''
    Test class for Credential class behaviours.
    Args:
        unittest.Testcase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_credential = Credential("Twitter", "mypassword")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test has run.
        '''
        Credential.credential_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.acc_name,"Twitter")
        self.assertEqual(self.new_credential.acc_password,"mypassword")

    def test_save_user(self):
        '''
        test_save_credential method to save credential
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1) 

    def test_delete_credential(self):

        '''
        test_delete_credential to remove credentials from our list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Twitter","mypassword")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)  

    # def test_display_credentials(self):
    #     '''
    #     method that returns a list of all user's credentials
    #     '''

    #     self.assertEqual(Credential.display_credentials("kadas"),Credential.credential_list)    
       
  

if __name__ == '__main__':
    unittest.main()