import unittest
import os
from ..src.Main import Main
import testbook

from ..src.helper import *

class Test_main(unittest.TestCase):

    # Initialize test object
    def __init__(self, *args, **kwargs):
        super(Test_main, self).__init__(*args, **kwargs)
        self.script_dir = self.get_script_dir()

        self.main = Main()
        print(f"self.main.addTwo(3)={self.main.addTwo(3)}")

    # returns the directory of this script regardles of from which level the code is executed
    def get_script_dir(self):
        return os.path.dirname(__file__)

    # tests unit test on addTwo function of main class
    def test_addTwo(self):

        expected_result = 7
        result = self.main.addTwo(5)
        self.assertEqual(expected_result, result)

    def test_create_emtpy_pin_connection_matrix_dictionary(self):
        rows=[]
        row_0=["a","b","c"]
        row_1=["d","e","f"]
        rows.append(row_0)
        rows.append(row_1)
        
        dictionary=create_emtpy_pin_connection_matrix_dictionary(rows)
        self.assertEqual(dictionary["a"],None)
        self.assertEqual(dictionary["b"],None)
        self.assertEqual(dictionary["c"],None)
        self.assertEqual(dictionary["d"],None)
        self.assertEqual(dictionary["e"],None)
        self.assertEqual(dictionary["f"],None)

    def test_verify_keys(self):
        rows=get_right_keys()
        
        dictionary=create_emtpy_pin_connection_matrix_dictionary(rows)
        self.assertEqual(dictionary["Spacebar (left half of right bar)"],None)
        self.assertEqual(dictionary["Spacebar (right half of right bar)"],None)
        self.assertEqual(dictionary["k"],None)
        self.assertEqual(dictionary["'"],None)
        self.assertEqual(dictionary["\\"],None)
        self.assertEqual(dictionary["/"],None)

if __name__ == "__main__":
    unittest.main()
