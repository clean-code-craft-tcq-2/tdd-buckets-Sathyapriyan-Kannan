import unittest
import test_driven_ranges


class TestDrivenRangesTest(unittest.TestCase):
    def test_valid_input(self):
        self.assertTrue(test_driven_ranges.is_valid_input([1, 2]))
        self.assertFalse(test_driven_ranges.is_valid_input([]))

    def test_get_range(self):
        self.assertEqual(test_driven_ranges.get_continuous_ranges([3, 3, 5, 4, 10, 11, 12]), ['3-5, 4', '10-12, 3'])
        self.assertEqual(test_driven_ranges.get_continuous_ranges([]), 'INVALID_INPUTS')
        self.assertEqual(test_driven_ranges.get_continuous_ranges([3]), [])
        self.assertEqual(test_driven_ranges.get_continuous_ranges([3, 4]), ['3-4, 2'])

    def test_get_most_frequent_reading(self):
        self.assertEqual(test_driven_ranges.get_most_frequent_reading([3, 4, 5, 7, 7, 7, 7, 20,21,22]), 7)

unittest.main()
