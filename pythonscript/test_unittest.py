# test_unittest.py
import unittest
from test_calc import add


class TestAdd(unittest.TestCase):
    def test_add(self):
    	test_patterns = [(1,3,4), (-2, 5, 3), (-3, -2, -5)]
    	for a, b, c in test_patterns:
	        res = add(a, b)
	        with self.subTest(res=res, c=c):
		        self.assertEqual(res, c)


if __name__ == "__main__":
    unittest.main()