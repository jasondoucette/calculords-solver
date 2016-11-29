from itertools import permutations, product, repeat
import random
from attempt import Attempt
from util import interleave

class Exhaustive(object):
    def solve(self, inputs, targets):
        digits = list(int(n) for n in inputs)
        perms = set(permutations(digits, len(digits)))
        ops = set(product(*repeat('-+*', len(digits) - 1)))

        c = 0
        winner = None
        for p in perms:
            for op in ops:
                attempt = Attempt('Exhaustive',
                                  interleave(list(p), list(op)),
                                  targets)
                result = attempt.run()
                if winner is None or winner.score() < result.score():
                    winner = result
                if winner.solved() is True:
                    break
                c += 1
            if winner.solved() is True:
                break
        return (winner, c)
