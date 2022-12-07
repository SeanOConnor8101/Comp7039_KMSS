import unittest
import COMP7039_CI_Code_BaseV1_0

"""
    - a class that inherits from unittest.testcase
    - gives us testing capabilities for our test class
"""


class Test_COMP7039_CI_Code_BaseV1_0(unittest.TestCase):

    txt_file_path = "CI_Project_Data_Files/"

    def test_read_integer_between_numbers(self):
        result = COMP7039_CI_Code_BaseV1_0.read_integer_between_numbers(
            prompt="Number is not between 1 and 7: ", mini=1, maximum=7)
        self.assertIn(result, 7 >= result >= 1)

    def test_read_nonempty_string(self):
        result = COMP7039_CI_Code_BaseV1_0.read_nonempty_string(
            prompt="Number is a empty string: ")
        self.assertNotEqual(result, '')

    def test_runners_data(self):
        runners_name, runners_id = COMP7039_CI_Code_BaseV1_0.runners_data()
        self.assertEqual(runners_name[0], "Anna Fox")
        self.assertEqual(runners_id[1], "CK-24")

    def test_read_integer(self):
        # error message in case if test case got failed
        message = "first value is not greater or equal than second value."
        result = COMP7039_CI_Code_BaseV1_0.read_integer(prompt=2)
        self.assertGreaterEqual(result, 0, message)

if __name__ == 'main':
    unittest.main()
