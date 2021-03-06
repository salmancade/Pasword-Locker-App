import unittest
from credential import Credential


class TestCredential(unittest.TestCase):
    """Test class that defines test cases for the Credentials class behavior
    """

    def setUp(self):
        """Set up method to run befor before each test case"""
        self.new_credentials = Credential("Facebook", "12345","0751996882")

    def test_credentials_instance(self):
        """Method that tests whether the new_credentials have been instantiated correctly"""
        self.assertEqual(self.new_credentials.account_name, "Facebook")
        self.assertEqual(self.new_credentials.account_password, "12345")
        self.assertEqual(self.new_credentials.account_phone, "0751996882")

    def test_save_credentials(self):
        """Method that tests whether the new credential created has been saved"""
        self.new_credentials.save_credential()
        self.assertEqual(len(Credential.credentials_list), 1)

    def test_save_multiple_credentials(self):
        """Method that saves multiple credentials to credentials_list"""
        self.new_credentials.save_credential()
        new_test_credential = Credential("Twitter", "56789","0712345678")
        new_test_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list), 2)

    def tearDown(self):
        """Method that clears the credentials_list after every test to ensure that there is no error"""
        Credential.credentials_list = []

    def test_find_credential_by_name(self):
        """Test to check if we can find credentials and display information"""
        self.new_credentials.save_credential()
        new_test_credential = Credential("Twitter", "56789","0745672315")
        new_test_credential.save_credential()

        found_credential = Credential.find_by_phone("0745672315")

        self.assertEqual(found_credential.account_name, new_test_credential.account_name)

    def test_display_all_credentials(self):
        """TestCase to test whether all contacts can be displayed"""
        self.assertEqual(Credential.display_credentials(), Credential.credentials_list)


if __name__ == '__main__':
    unittest.main()