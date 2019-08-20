import extract
import unittest
import random

class TestExtract(unittest.TestCase):
    def setUp(self):
        pass
    def test_round_half_up(self):
        r = range(0, 2)
        nb_to_test = extract.round_half_up(random.uniform(0, 1))
        self.assertTrue(nb_to_test in r)
    def test_fetch_imgs(self):
        ig = extract.imgs_gen()
        self.assertTrue(next(ig))

if __name__ == '__main__':
    unittest.main()