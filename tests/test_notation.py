from unittest import TestCase

from chancetoroll import notation


class TestParseDstr(TestCase):
    def test_3d6(self):
        self.assertEqual(notation.parse_dstr("3d6"), (3, 6))

    def test_1d20(self):
        self.assertEqual(notation.parse_dstr("1d20"), (1, 20))

    def test_4d8(self):
        self.assertEqual(notation.parse_dstr("4d8"), (4, 8))

    def test_bad_str(self):
        with self.assertRaises(IndexError):
            notation.parse_dstr("123")

    def test_partial_str(self):
        with self.assertRaises(ValueError):
            notation.parse_dstr("2d")
