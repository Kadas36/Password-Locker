import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class for user class behaviours.
    Args:
        unittest.Testcase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_user = User( "JohnDoe", "DoeJohn36", "johndoe@gmail.com")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test has run.
        '''
        User.user_list = []

    # def test_init(self):
    #     '''
    #     test_init test case to test if the object is initialized properly
    #     '''

    #     self.assertEqual(self.new_user.username,"JohnDoe")
    #     self.assertEqual(self.new_user.email,"johndoe@gmail.com")
    #     self.assertEqual(self.new_user.password,"DoeJohn36")

    # def test_save_user(self):
    #     '''
    #     test_save_user method to save a user
    #     '''
    #     self.new_user.save_user()
    #     self.assertEqual(len(User.user_list),1)


    # def test_find_user_by_username(self):
    #     '''
    #     test to check if we can find a user by their user name.
    #     '''
    #     self.new_user.save_user()
    #     test_user = User("JohnDoe", "JohnDoe36", "johndoe@gmail.com")
    #     test_user.save_user()

    #     found_user = User.find_by_username("JohnDoe")

    #     self.assertEqual(found_user.email,test_user.email)

    # def test_contact_exists(self):
    #     '''
    #     test to check if we can return a Boolean  if we cannot find the contact.
    #     '''

    #     self.new_user.save_user()
    #     decoy_user = User("kadas", "kadas@hotmail.com", "kadas36") 
    #     decoy_user.save_user()

    #     user_exists = User.user_exists("kadas")

    #     self.assertTrue(user_exists)    

if __name__ == '__main__':
    unittest.main()