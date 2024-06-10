import unittest
from unittest.mock import patch
from functions.compose_main_menu import main_menu
from classes.user_manager import UserManager
from classes.user import User

class TestMainMenu(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'testuser', 'password123', 'test@example.com', '25', '70', '175', 'moderately active', 'male', '3'])
    @patch('builtins.print')
    @patch.object(UserManager, 'sign_up')
    def test_sign_up(self, mock_sign_up, mock_print, mock_input):
        mock_sign_up.return_value = User(user_id=1, username='testuser', password='hashedpassword', email='test@example.com', age=25, weight=70, height=175, activity_level='moderately active', gender='male')
        main_menu()
        self.assertTrue(mock_sign_up.called)
        mock_print.assert_any_call("User testuser signed up successfully with ID: 1")

    @patch('builtins.input', side_effect=['2', 'testuser', 'password123', '3'])
    @patch('builtins.print')
    @patch.object(UserManager, 'sign_in')
    def test_sign_in_success(self, mock_sign_in, mock_print, mock_input):
        mock_sign_in.return_value = True
        with patch('functions.compose_profile_menu.user_profile_menu', return_value=None):
            main_menu()
        self.assertTrue(mock_sign_in.called)
        mock_print.assert_any_call("Sign in successful!")

    @patch('builtins.input', side_effect=['2', 'testuser', 'wrongpassword', '3'])
    @patch('builtins.print')
    @patch.object(UserManager, 'sign_in')
    def test_sign_in_failure(self, mock_sign_in, mock_print, mock_input):
        mock_sign_in.return_value = False
        main_menu()
        self.assertTrue(mock_sign_in.called)
        mock_print.assert_any_call("Invalid username or password.")

    @patch('builtins.input', side_effect=['3'])
    @patch('builtins.print')
    def test_exit(self, mock_print, mock_input):
        main_menu()
        mock_print.assert_any_call("3. Exit")


if __name__ == '__main__':
    unittest.main()
