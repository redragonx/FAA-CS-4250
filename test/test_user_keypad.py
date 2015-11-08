import unittest
from io_package.user_keypad import User_keypad

__author__ = 'group'


class TestUserKeypad(unittest.TestCase):


    def test_keypad_input(self):

        keypad = User_keypad()

        test_string1 = '4538#'
        test_string2 = '453#'
        test_string3 = '#4567'
        test_string4 = '453556#'
        test_string5 = '453#6'
        test_string6 = '#453#'
        test_string7 = '4536#45'


    # test to see if a good input is processed correctly
        self.assertEqual('Success', keypad.keypad_input(test_string1), "Test 1 Failed")

    # tests 2-7 to see if a bad input is processed correctly
        self.assertEqual('Fail', keypad.keypad_input(test_string2), "Test 2 Failed")
        self.assertEqual('Fail', keypad.keypad_input(test_string3), "Test 3 Failed")
        self.assertEqual('Fail', keypad.keypad_input(test_string4), "Test 4 Failed")
        self.assertEqual('Fail', keypad.keypad_input(test_string5), "Test 5 Failed")
        self.assertEqual('Fail', keypad.keypad_input(test_string6), "Test 6 Failed")
        self.assertEqual('Fail', keypad.keypad_input(test_string7), "Test 7 Failed")

if __name__ == '__main__':
    unittest.main()
