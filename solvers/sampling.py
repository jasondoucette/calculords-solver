from itertools import product, repeat
from random import choice, shuffle
from attempt import Attempt
from util import interleave

class Sampling(object):
    def __init__(self):
        self.cycles = 100000

    def solve(self, inputs, targets):
        digits = list(int(n) for n in inputs)
        winner = None
        c = 0
        for n in range(self.cycles):
            shuffle(digits)
            ops = choice(list(product(*repeat('-+*', len(digits) - 1))))

            attempt = Attempt('Sampling',
                              interleave(list(digits), list(ops)),
                              targets)
            result = attempt.run()
            if winner is None or result.score() > winner.score():
                winner = result
            if winner.solved():
                break
            c = c + 1
        return (winner, c)
