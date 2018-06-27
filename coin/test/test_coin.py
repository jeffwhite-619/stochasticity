import unittest
import random
from stochasticity.coin.coin import Coin


class TestCoin(unittest.TestCase):
    _values = [True, False]

    def test_flip(self):
        test_flip = Coin.flip()
        self.assertIn(test_flip, self._values)
        flips = random.randrange(1, 500)
        test_flip = Coin.flip(flips)
        self.assertIn(test_flip, self._values)


if __name__ == '__main__':
    unittest.main()

