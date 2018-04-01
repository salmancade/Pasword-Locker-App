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

    if __name__ == '__main__':
        unittest.main()
