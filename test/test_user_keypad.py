import unittest
from io_package.user_keypad import User_keypad

__author__ = 'group'


class TestUserKeypad(unittest.TestCase):


    def test_keypad_input(self):

        keypad = User_keypad()

        test_string1 = '4538#'
        test_string2 = '453#'

        test1_answer = False
        test2_answer = False

    # test to see if a good input is processed correctly
        self.assertEqual('Success', keypad.keypad_input(test_string1), "Test 1 Failed")

    # test to see if a bad input is processed correctly
        self.assertEqual('Fail', keypad.keypad_input(test_string1), "Test 2 Failed")


if __name__ == '__main__':
    unittest.main()
