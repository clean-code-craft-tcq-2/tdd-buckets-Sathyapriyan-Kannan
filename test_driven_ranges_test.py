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
        self.assertEqual(test_driven_ranges.get_threshold(12, is_signed=False), 4095)
        self.assertEqual(test_driven_ranges.get_threshold(12, is_signed=True), 2047)
        self.assertEqual(test_driven_ranges.get_threshold(10, is_signed=False), 1023)
        self.assertEqual(test_driven_ranges.get_threshold(10, is_signed=True), 511)

    def test_convert_a2d_to_amp(self):
        self.assertEqual(
            test_driven_ranges.convert_a2d_to_amp(1048, test_driven_ranges.get_threshold(12, is_signed=False), 10,
                                                  is_signed=False), 3)
        self.assertEqual(
            test_driven_ranges.convert_a2d_to_amp(4094, test_driven_ranges.get_threshold(12, is_signed=False), 10,
                                                  is_signed=False), 10)
        self.assertEqual(
            test_driven_ranges.convert_a2d_to_amp(0, test_driven_ranges.get_threshold(10, is_signed=True), 15,
                                                  is_signed=True), 15)
        self.assertEqual(
            test_driven_ranges.convert_a2d_to_amp(1023, test_driven_ranges.get_threshold(10, is_signed=True), 15,
                                                  is_signed=True), 15)
        self.assertEqual(
            test_driven_ranges.convert_a2d_to_amp(550, test_driven_ranges.get_threshold(10, is_signed=True), 15,
                                                  is_signed=True), 1)

    def test_remove_error_readings(self):
        self.assertEqual(test_driven_ranges.remove_error_readings([1000, 1005, 1200, 1494, 4094, 4095], 12),
                         [1000, 1005, 1200, 1494, 4094])
        self.assertEqual(test_driven_ranges.remove_error_readings([1000, 1005, 1200, 1494, 4094, 4095], 10),
                         [1000, 1005])

    def test_convert_a2d_readings_into_current(self):
        self.assertEqual(test_driven_ranges.convert_a2d_readings_into_current(
            [1000, 1005, 1200, 1494, 4094, 4095], 12, 10, is_signed=False), [2, 2, 3, 4, 10])

        self.assertEqual(test_driven_ranges.convert_a2d_readings_into_current(
            [1001, 1006, 1201, 1495, 4094, 4095], 10, 15, is_signed=True), [14, 15])

        self.assertEqual(test_driven_ranges.convert_a2d_readings_into_current(
            [1150, 1200, 1225, 1494], 12, 10, is_signed=False), [3, 3, 3, 4])

    def test_get_continuous_ranges_from_a2d_sensor(self):
        self.assertEqual(test_driven_ranges.get_continuous_ranges_from_a2d_sensor(
            [], 12, 10, is_signed=False), 'INVALID_INPUTS')
        self.assertEqual(test_driven_ranges.get_continuous_ranges_from_a2d_sensor(
            [], 12, 10, is_signed=True), 'INVALID_INPUTS')
        self.assertEqual(test_driven_ranges.get_continuous_ranges_from_a2d_sensor(
            [], 10, 15, is_signed=False), 'INVALID_INPUTS')
        self.assertEqual(test_driven_ranges.get_continuous_ranges_from_a2d_sensor(
            [], 10, 15, is_signed=True), 'INVALID_INPUTS')
        self.assertEqual(
            test_driven_ranges.get_continuous_ranges_from_a2d_sensor(
                [1000, 1005, 1200, 1494, 4094, 4095], 12, 10, is_signed=False), ['2-4, 4'])
        self.assertEqual(
            test_driven_ranges.get_continuous_ranges_from_a2d_sensor(
                [0, 12, 55, 70, 1005, 1200, 1494, 2095, 3890, 4094, 4095], 12, 10, is_signed=True),
                ['3-5, 3', '9-10, 6'])
        self.assertEqual(
            test_driven_ranges.get_continuous_ranges_from_a2d_sensor(
                [0, 44, 100, 150, 511, 600, 750], 10, 15, is_signed=True), ['11-12, 2', '14-15, 2'])
        self.assertEqual(
            test_driven_ranges.get_continuous_ranges_from_a2d_sensor(
                [0, 43, 101, 151, 511, 601, 751, 1500], 12, 10, is_signed=False), ['0-2, 7'])

    def test_get_max_possible_reading(self):
        self.assertEqual(test_driven_ranges.get_max_possible_reading(10), 1023)
        self.assertEqual(test_driven_ranges.get_max_possible_reading(12), 4095)


unittest.main()
