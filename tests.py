import unittest

from divider import divide, search


class TestDiveder(unittest.TestCase):
    def test_zero(self):
        self.assertRaises(Exception, lambda : divide(0,0))

    def test_zero_one(self):
        self.assertEqual(divide(0, 1), 0)

    def test_one_two(self):
        self.assertEqual(divide(2, 1), 2)

    def test_search(self):
        self.assertEqual(search(2, 10), 5)

    def test_search39(self):
        self.assertEqual(search(3, 9), 3)

    def test_search310(self):
        self.assertEqual(search(3, 10), 3)

    def test_search_cray(self):
        self.assertEqual(search(23, 4564334), int(4564334 / 23))

    def test_positive_by_one(self):
        self.assertEqual(divide(300, 1), 300)

    def test_negative_by_one(self):
        self.assertEqual(divide(300, -1), -300)

    def test_test_remainder(self):
        self.assertEqual(divide(5, 2), [2, 1])

    def test_stco_1(self):
        self.assertEqual(divide(6, 5), [1, 1])

    def test_stco_2(self):
        self.assertEqual(divide(6, -5), [-2, -4])

    def test_stco_3(self):
        self.assertEqual(divide(-6, 5), [-2, 4])

    def test_stco_4(self):
        self.assertEqual(divide(-6, -5), [1, 1])
