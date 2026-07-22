import unittest

from analytics_assignment.calculations import (
    car_arrival_probability,
    expected_distinct_species,
    expected_double_winners,
    pearson_correlation,
    roc_auc,
)
from analytics_assignment.python_tasks import is_isomorphic, missing_number, prime_factors


class PythonTaskTests(unittest.TestCase):
    def test_isomorphic_true_cases(self):
        self.assertTrue(is_isomorphic("paper", "title"))
        self.assertTrue(is_isomorphic("egg", "add"))
        self.assertTrue(is_isomorphic("", ""))

    def test_isomorphic_false_cases(self):
        self.assertFalse(is_isomorphic("foo", "bar"))
        self.assertFalse(is_isomorphic("ab", "aa"))
        self.assertFalse(is_isomorphic("abc", "de"))

    def test_missing_number(self):
        self.assertEqual(missing_number([1, 2, 3, 4, 5, 6, 8, 9, 10, 11]), 7)
        self.assertEqual(missing_number([2, 3, 4]), 1)
        self.assertEqual(missing_number([1, 2, 3]), 4)

    def test_prime_factors(self):
        self.assertEqual(prime_factors(1), [])
        self.assertEqual(prime_factors(2), [2])
        self.assertEqual(prime_factors(56), [2, 2, 2, 7])
        self.assertEqual(prime_factors(97), [97])
        with self.assertRaises(ValueError):
            prime_factors(0)


class CalculationTests(unittest.TestCase):
    def test_probability_answers(self):
        self.assertAlmostEqual(expected_distinct_species(), 3.990612, places=6)
        self.assertAlmostEqual(expected_double_winners(), 26.835443, places=6)
        self.assertAlmostEqual(car_arrival_probability(0.95, 30, 10) * 100, 63.159685, places=6)
        self.assertAlmostEqual(car_arrival_probability(0.95, 30, 27) * 100, 93.253586, places=6)

    def test_ml_metric_answers(self):
        labels = [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0]
        scores = [0.95, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25]
        cups = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
        exam_scores = [85, 88, 79, 81, 84, 65, 67, 58, 76, 49]
        self.assertAlmostEqual(roc_auc(labels, scores), 0.75)
        self.assertAlmostEqual(pearson_correlation(cups, exam_scores), -0.8492696876732622)


if __name__ == "__main__":
    unittest.main()
