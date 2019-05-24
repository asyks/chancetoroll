from unittest import TestCase

from chancetoroll import rollem


class TestCalcSuccessProbability(TestCase):
    def test_2d6_target_1(self):
        self.assertEqual(
            rollem.calc_success_probability(typedice=6, numdice=2, targetside=1), 1.0
        )

    def test_2d6_target_3(self):
        self.assertAlmostEqual(
            rollem.calc_success_probability(typedice=6, numdice=2, targetside=3),
            0.9333333333,
            places=10,
        )

    def test_2d6_target_6(self):
        self.assertAlmostEqual(
            rollem.calc_success_probability(typedice=6, numdice=2, targetside=6),
            0.3333333333,
            places=10,
        )

    def test_d10_target_1(self):
        self.assertEqual(
            rollem.calc_success_probability(typedice=10, numdice=3, targetside=1), 1.0
        )

    def test_3d10_target_5(self):
        self.assertAlmostEqual(
            rollem.calc_success_probability(typedice=10, numdice=3, targetside=5),
            0.9666666667,
            places=10,
        )

    def test_3d10_target_10(self):
        self.assertEqual(
            rollem.calc_success_probability(typedice=10, numdice=3, targetside=10), 0.3
        )
