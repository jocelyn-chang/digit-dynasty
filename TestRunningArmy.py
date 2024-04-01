import pygame, unittest
from RunningArmy import check_answer, generate_arrows, instruction1
from Player import Player
from Question import Question
from unittest.mock import patch


class TestRunningArmy(unittest.TestCase):

    def test_check_answer_correct(self):
        """
        Tests that the check answer can detect a correct answer
        """
        self.assertTrue(check_answer("6", "6"))

    def test_check_answer_incorrect(self):
        """
        Tests that the check answer can detect an incorrect answer
        """
        self.assertFalse(check_answer("5", "6"))

    def test_generate_arrows_case_1(self):
        """
        Tests that the correct number of arrows are generated
        """
        self.assertEqual(generate_arrows(0, 3), 1)

    def test_generate_arrows_case_2(self):
        """
        Tests that the correct number of arrows are generated
        """
        self.assertEqual(generate_arrows(0, 5), 2)

    def test_generate_arrows_case_3(self):
        """
        Tests that the correct number of arrows are generated
        """
        self.assertEqual(generate_arrows(0, 7), 3)

    def test_generate_arrows_case_4(self):
        """
        Tests that the correct number of arrows are generated
        """
        self.assertEqual(generate_arrows(0, 9), 4)

    def test_generate_arrows_case_5(self):
        """
        Tests that the correct number of arrows are generated
        """
        self.assertIn(generate_arrows(0, 11), range(1, 16))

    def test_generate_arrows_incorrect_counter(self):
        """
        Tests that the correct number of arrows are generated when an incorrect answer is given
        """
        self.assertGreaterEqual(generate_arrows(1, 5), 6)

    def test_player_score_update(self):
        """
        Tests that the players score is correctly updated
        """
        player = Player("test_user", "test_password")
        player.update_mul("5")
        self.assertEqual(player.get_mul(), "5")

    def test_question_generation(self):
        """
        Tests that the game generates the correct questions
        """
        player = Player("test_user", "test_password")
        question = Question(player)
        self.assertIsInstance(question.generate_question('*'), tuple)

    def test_question_answer_validation(self):
        """
        Tests the integration of question and check answer
        """
        player = Player("test_user", "test_password")
        question = Question(player)
        question_text = question.generate_question('*')
        self.assertTrue(check_answer(str(question_text[0] * question_text[1]), str(question_text[0] * question_text[1])))
    
    def test_question_generation_multiplication(self):
        """
        Tests that the game generates the correct questions
        """
        player = Player("test_user", "test_password")
        question = Question(player)
        generated_question = question.generate_question('*')
        self.assertIsInstance(generated_question, tuple)
        self.assertEqual(len(generated_question), 2)
        self.assertIsInstance(generated_question[0], int)
        self.assertIsInstance(generated_question[1], int)
    
    def test_panda_arrow_change_after_gate(self):
        """
        Ensuring the number and pandas and arrows change after entering a gate
        """
        # Initial conditions
        num_pandas = 3
        incorrect_counter = 0

        # Simulate the panda entering a gate
        num_arrows = generate_arrows(incorrect_counter, num_pandas)
        if num_arrows >= num_pandas:
            # Panda loses, no change in number of pandas
            self.assertEqual(num_pandas, 3)
        else:
            # Panda wins, number of pandas should decrease
            num_pandas -= num_arrows
            self.assertLess(num_pandas, 3)

        # Check that the number of arrows is updated for the next gate
        new_num_arrows = generate_arrows(incorrect_counter, num_pandas)
        self.assertNotEqual(new_num_arrows, num_arrows)
    
    @patch('RunningArmy.instruction1')
    def test_back_button_click(self, mock_instruction1):
        """
        Tests the game's handling of the 'back' button event, simulating a user clicking
        the back button and verifying that the game responds as expected.
        """
        # Simulate clicking the back button
        with patch('pygame.event.get') as mock_event_get:
            mock_event_get.return_value = [pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': (70, 55)})]
            instruction1()

        # Verify that the instruction1 function is called, simulating going back to the instruction screen
        mock_instruction1.assert_called_once()

if __name__ == '__main__':
    unittest.main()
