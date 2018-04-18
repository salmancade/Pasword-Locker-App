import unittest # Importing the unnitest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test case for the contact class behaviours

    Args:
      unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def test_setUp(self):
        self.new_user = User("mariam","Omar","0712345645","mariam@cm","mimimom")
    def test_init(self):
        self.assertEqual(self.new_user.first_name,"mariam")
        self.assertEqual(self.new_user.last_name, "0712345645")
        self.assertEqual(self.new_user.last_name, "Omar")
        self.assertEqual(self.new_user.email, "mariam@cm")
        self.assertEqual(self.new_user.password, "mimimom")

    def test_init_(self):
        
        '''
        test case to if the User object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name, "mariam")
        self.assertEqual(self.new_user.password, "password")

    def test_save_user(self):

        '''
        test case to test if user objects have been saved into user_list
        '''

        self.new_user.save_user()  # save new user
        self.assertEqual(len(User.user_list), 1)

     # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_save_multiple_user(self):
        '''
        tst_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","0712345678","test@user.com","password")
        self.assertEqual(len(User.user_list),2)
    


if __name__ == '__main__':
    unittest.main()
