import unittest
import test_driven_ranges


class TestDrivenRangesTest(unittest.TestCase):
    def test_valid_input(self):
        self.assertTrue(test_driven_ranges.is_valid_input([1, 2]))
        self.assertFalse(test_driven_ranges.is_valid_input([]))

    def test_get_range(self):
        self.assertEqual(test_driven_ranges.get_continuous_ranges([3, 3, 5, 4, 10, 11, 12]), ['3-5, 4', '10-12, 3'])
        self.assertEqual(test_driven_ranges.get_continuous_ranges([]), 'INVALID_INPUTS')

if __name__ == '__main__':
    unittest.main()