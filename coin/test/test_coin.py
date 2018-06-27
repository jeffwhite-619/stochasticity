import random


class Coin:
    @staticmethod
    def flip(flips: int = 0):
        if flips < 1:
            flips = random.randint(1, 50)
        coinflip = random.choice([True, False])
        if flips > 1:
            for i in range(flips - 1):
                coinflip = random.choice([True, False])
        return coinflip
