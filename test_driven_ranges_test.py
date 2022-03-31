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
        self.assertEqual(test_driven_ranges.get_most_frequent_reading([3, 4, 5, 7, 7, 7, 7, 20, 21, 22]), 7)
        self.assertEqual(test_driven_ranges.get_most_frequent_reading([]), 'INVALID_INPUTS')

    def test_get_threshold(self):
        self.assertEqual(test_driven_ranges.get_threshold(12), 4095)

    def test_convert_a2d_to_amp(self):
        self.assertEqual(test_driven_ranges.convert_a2d_to_amp(1048, test_driven_ranges.get_threshold(12)), 3)
        self.assertEqual(test_driven_ranges.convert_a2d_to_amp(0, test_driven_ranges.get_threshold(12)), 0)

    def test_remove_error_readings(self):
        self.assertEqual(test_driven_ranges.remove_error_readings([1000, 1005, 1200, 1494, 4094, 4095],
                                                                  test_driven_ranges.get_threshold(12)),
                         [1000, 1005, 1200, 1494, 4094])

    def test_convert_a2d_readings_into_current(self):
        self.assertEqual(test_driven_ranges.convert_a2d_readings_into_current([1000, 1005, 1200, 1494, 4094, 4095], 12),
                         [2, 2, 3, 4, 10])
        self.assertEqual(test_driven_ranges.convert_a2d_readings_into_current([1150, 1200, 1225, 1494], 12),
                         [3, 3, 3, 4])

    def test_get_continuous_ranges_from_a2d_sensor(self):
        self.assertEqual(
            test_driven_ranges.get_continuous_ranges_from_a2d_sensor([1000, 1005, 1200, 1494, 4094, 4095], 12),
            ['2-4, 4'])
        self.assertEqual(test_driven_ranges.get_continuous_ranges_from_a2d_sensor([], 12), 'INVALID_INPUTS')


unittest.main()
