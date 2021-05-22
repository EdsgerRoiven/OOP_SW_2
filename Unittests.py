import unittest
from Circle import *
from Rectangle import *
class Unittest(unittest.TestCase):
    def test_dawn(self):
        basic_circle = Circle(10)
        expected_circle = copy.copy(basic_circle)
        result_circle = Circle(10)
        self.assertEqual(expected_circle.radius,result_circle.radius)
    def test_up(self):
        basic_rectangle = Rectangle(10,20)
        expected_rectangle = copy.copy(basic_rectangle)
        result_rectangle = Rectangle(10,10)
        self.assertEqual(expected_rectangle.height,result_rectangle.height)
if __name__ == '__main__':
    unittest.main(verbosity=2)