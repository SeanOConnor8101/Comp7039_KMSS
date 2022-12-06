import unittest
import COMP7039_CI_Code_BaseV1_0

"""
    - a class that inherits from unittest.testcase
    - gives us testing capabilities for our test class
"""


class Test_COMP7039_CI_Code_BaseV1_0(unittest.TestCase):

    def test_read_integer_between_numbers(self):
        result = COMP7039_CI_Code_BaseV1_0.read_integer_between_numbers(
            prompt="Number is not between 1 and 7",                                                  mini=1,                                                maximum=7)
        self.assertIn(result, 7 >= result >= 1)


if __name__ == 'main':
    unittest.main()
