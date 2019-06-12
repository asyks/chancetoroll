from unittest import TestCase

from chancetoroll import calc


class TestCalcSuccessProbability(TestCase):
    def test_1d6_target_6(self):
        self.assertEqual(
            calc.calc_success_probability(size=6, k=1, target=6),
            1.0 / 6
        )

    def test_1d8_target_8(self):
        self.assertEqual(
            calc.calc_success_probability(size=8, k=1, target=8),
            1.0 / 8
        )

    def test_2d6_target_1(self):
        self.assertEqual(
            calc.calc_success_probability(size=6, k=2, target=1), 1.0
        )

    def test_2d6_target_3(self):
        self.assertAlmostEqual(
            calc.calc_success_probability(size=6, k=2, target=3),
            0.9333333333,
            places=10,
        )

    def test_2d6_target_6(self):
        self.assertAlmostEqual(
            calc.calc_success_probability(size=6, k=2, target=6),
            0.3333333333,
            places=10,
        )

    def test_d10_target_1(self):
        self.assertEqual(
            calc.calc_success_probability(size=10, k=3, target=1), 1.0
        )

    def test_3d10_target_5(self):
        self.assertAlmostEqual(
            calc.calc_success_probability(size=10, k=3, target=5),
            0.9666666667,
            places=10,
        )

    def test_3d10_target_10(self):
        self.assertEqual(
            calc.calc_success_probability(size=10, k=3, target=10), 0.3
        )
