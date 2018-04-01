import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):

        self.new_user = User("mariam","Omar","0712345678","mariam@cm","")


    def test_init(self):
        self.assertEqual(self.new_user.first_name,"mariam")
        self.assertEqual(self.new_user.last_name, "Omar")
        self.assertEqual(self.new_user.phone, "072345678")
        self.assertEqual(self.new_user.email, "mariam@cm")
        self.assertEqual(self.new_user.password, "")

    def test_init_(self):

        '''
        test case to if the User object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name, "seth")
        self.assertEqual(self.new_user.password, "password")

    def test_save_user(self):

        '''
        test case to test if user objects have been saved into user_list
        '''

        self.new_user.save_user()  # save new user
        self.assertEqual(len(User.user_list), 1)


    if __name__ == '__main__':
        unittest.main()
