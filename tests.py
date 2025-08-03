import unittest

from index import Tomato, TOMATO_LIST
from config import MAX_PRICE, MIN_PRICE


class TestTomato(unittest.TestCase):

    def setUp(self):
        TOMATO_LIST.clear()

    def test_filter_by_gt(self):
        TOMATO_LIST.append(Tomato(8, ""))
        TOMATO_LIST.append(Tomato(10, ""))
        TOMATO_LIST.append(Tomato(2, ""))

        result = Tomato.filter_by(price__gt=5)

        for tomato in result:
            self.assertGreater(tomato.price, 5)

        self.assertEqual(len(result), 2)

    def test_filter_by_lt(self):
        TOMATO_LIST.append(Tomato(3, ""))
        TOMATO_LIST.append(Tomato(7, ""))
        TOMATO_LIST.append(Tomato(6, ""))

        result = Tomato.filter_by(price__lt=7)

        for tomato in result:
            self.assertLess(tomato.price, 7)

        self.assertEqual(len(result), 2)

    def test_generate_tomatoes(self):
        tomatoes = Tomato(0, "").generate_fake_tomatoes(times=20)
        self.assertEqual(len(tomatoes), 20)

        for tomato in tomatoes:
            self.assertGreaterEqual(tomato.price, MIN_PRICE)
            self.assertLessEqual(tomato.price, MAX_PRICE)


if __name__ == "__main__":
    unittest.main()
