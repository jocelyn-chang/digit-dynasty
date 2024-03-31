import unittest
from unittest.mock import patch, mock_open
from mainMenu import append_to_csv, username_exists, validate_username, validate_password, load_player

class TestMainMenu(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    def test_append_to_csv(self, mock_file):
        append_to_csv('testuser', 'testpass')
        mock_file.assert_called_with('data.csv', 'a', newline='')
        mock_file().write.assert_called_once()

    @patch('mainMenu.csv.reader')
    def test_username_exists(self, mock_csv_reader):
        mock_csv_reader.return_value = iter([['testuser', 'testpass']])
        self.assertTrue(username_exists('testuser'))
        self.assertFalse(username_exists('nonexistentuser'))

    def test_validate_username(self):
        self.assertTrue(validate_username('validUser123'))
        self.assertFalse(validate_username('invalid user'))
        self.assertFalse(validate_username('!@#$%'))

    def test_validate_password(self):
        self.assertTrue(validate_password('ValidPass123'))
        self.assertFalse(validate_password('short'))
        self.assertFalse(validate_password('toolongpassworddefinitely'))
        self.assertFalse(validate_password('no$ymb0l$'))
    
    @patch("builtins.open", mock_open(read_data="username,password,0,0,0,0,0\nanotheruser,pass,1,1,1,1,1"))
    def test_load_player(self):
        self.assertIsNotNone(load_player('username', 'password'))
        self.assertIsNone(load_player('nonexistentuser', 'nopass'))

if __name__ == "__main__":
    unittest.main()