from random import randint
import time


class Dice:
    """Game Dice"""
    facet = 6

    def throw(self) -> int:
        """Return sum for dropped combination"""
        print('Throw!', end=' ')
        time.sleep(1)
        dice1 = randint(1, self.facet)
        dice2 = randint(1, self.facet)
        print(f'Dropped combination: {dice1} {dice2}')
        return dice1 + dice2
