import unittest
from unittest.mock import patch
from functions.compose_main_menu import main_menu
from classes.user_manager import UserManager
from classes.user import User

class TestMainMenu(unittest.TestCase):
    """
    Unit test class for testing the main menu functions related to user sign up, sign in, and exit options.
    """

    @patch('builtins.input', side_effect=['1', 'testuser', 'password123', 'test@example.com', '25', '70', '175', 'moderately active', 'male', '3'])
    @patch('builtins.print')
    @patch.object(UserManager, 'sign_up')
    def test_sign_up(self, mock_sign_up, mock_print, mock_input):
        """
        Tests the user sign up process in the main menu.

        This test mocks user input to simulate a user signing up, and verifies that the sign up process
        is called and prints a success message.

        Parameters:
        -----------
        mock_sign_up : MagicMock
            Mocked method of UserManager's sign_up.
        mock_print : MagicMock
            Mocked print function.
        mock_input : MagicMock
            Mocked input function with side effects to simulate user inputs.
        """
        mock_sign_up.return_value = User(user_id=1, username='testuser', password='hashedpassword', email='test@example.com', age=25, weight=70, height=175, activity_level='moderately active', gender='male')
        main_menu()
        self.assertTrue(mock_sign_up.called)
        mock_print.assert_any_call("User testuser signed up successfully with ID: 1")

    @patch('builtins.input', side_effect=['2', 'testuser', 'password123', '3'])
    @patch('builtins.print')
    @patch.object(UserManager, 'sign_in')
    def test_sign_in_success(self, mock_sign_in, mock_print, mock_input):
        """
        Tests the user sign in process with correct credentials in the main menu.

        This test mocks user input to simulate a successful sign in and verifies that the sign in process
        is called and prints a success message.

        Parameters:
        -----------
        mock_sign_in : MagicMock
            Mocked method of UserManager's sign_in.
        mock_print : MagicMock
            Mocked print function.
        mock_input : MagicMock
            Mocked input function with side effects to simulate user inputs.
        """
        mock_sign_in.return_value = True
        with patch('functions.compose_profile_menu.user_profile_menu', return_value=None):
            main_menu()
        self.assertTrue(mock_sign_in.called)
        mock_print.assert_any_call("Sign in successful!")

    @patch('builtins.input', side_effect=['2', 'testuser', 'wrongpassword', '3'])
    @patch('builtins.print')
    @patch.object(UserManager, 'sign_in')
    def test_sign_in_failure(self, mock_sign_in, mock_print, mock_input):
        """
        Tests the user sign in process with incorrect credentials in the main menu.

        This test mocks user input to simulate a failed sign in and verifies that the sign in process
        is called and prints an error message.

        Parameters:
        -----------
        mock_sign_in : MagicMock
            Mocked method of UserManager's sign_in.
        mock_print : MagicMock
            Mocked print function.
        mock_input : MagicMock
            Mocked input function with side effects to simulate user inputs.
        """
        mock_sign_in.return_value = False
        main_menu()
        self.assertTrue(mock_sign_in.called)
        mock_print.assert_any_call("Invalid username or password.")

    @patch('builtins.input', side_effect=['3'])
    @patch('builtins.print')
    def test_exit(self, mock_print, mock_input):
        """
        Tests the exit option in the main menu.

        This test mocks user input to simulate a user choosing to exit and verifies that the
        exit option is printed.

        Parameters:
        -----------
        mock_print : MagicMock
            Mocked print function.
        mock_input : MagicMock
            Mocked input function with side effects to simulate user inputs.
        """
        main_menu()
        mock_print.assert_any_call("3. Exit")


if __name__ == '__main__':
    unittest.main()
