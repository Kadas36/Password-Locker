import unittest
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
        self.new_credential = Credential( "Twitter", "mypassword")

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
  

if __name__ == '__main__':
    unittest.main()