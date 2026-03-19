import unittest

from failing_calculator import average_ratios


class AverageRatiosTests(unittest.TestCase):
    def test_regular_values(self):
        self.assertAlmostEqual(average_ratios([10, 5]), 15.0)

    def test_ignores_zero_values(self):
        self.assertAlmostEqual(average_ratios([10, 5, 0]), 15.0)

    def test_all_zeros_raises(self):
        with self.assertRaises(ValueError):
            average_ratios([0, 0])

    def test_empty_list_raises(self):
        with self.assertRaises(ValueError):
            average_ratios([])


if __name__ == "__main__":
    unittest.main()
