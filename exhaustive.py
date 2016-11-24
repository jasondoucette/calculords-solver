#!/usr/bin/env python

from itertools import ifilter, permutations, product, repeat
import random

inputs = '48497336'
targets = [28,35,63]

class Result(object):
    def __init__(self, actions, remainingInputs, remainingTargets):
        self.actions = actions
        self.remainingInputs = remainingInputs
        self.remainingTargets = remainingTargets

    def solved(self):
        return not (self.remainingTargets or self.remainingInputs)

    def score(self):
        if len(self.remainingTargets) > 3:
            return 0
        else:
            # Fewer targets is better than more targets (1 action means 1 target):
            targetScore = 10*(len(self.actions))
            # Fewer high targets is better than fewer low targets:
            targetScore -= sum(self.remainingTargets)
            # Prioritize fewer leftover inputs:
            inputScore = (10-len(self.remainingInputs))
            return targetScore + inputScore

    def __str__(self):
        return "Score: {}\nLeftover inputs: {}\nLeftover targets: {}\nActions:\n  {}\n\n".format(
            str(self.score()),
            ", ".join(str(i) for i in sorted(self.remainingInputs)),
            ", ".join(str(i) for i in sorted(self.remainingTargets)),
            "\n  ".join(self.actions))

class Attempt(object):
    def __init__(self, combination, targets):
        self.combination = combination
        self.targets = list(targets)

    def run(self):
        def walk(combination, ptr, actionsSoFar, remainingTargets):
            start = ptr
            targets = list(remainingTargets)
            actions = list(actionsSoFar)
            if ptr >= len(combination):
                return Result(actions, [], targets)

            alternate = None
            total = int(combination[ptr])
            while ptr < len(combination):
                if total in targets:
                    altTargets = list(targets)
                    altTargets.remove(total)
                    altActions = list(actions)
                    action = ''.join([str(n) for n in combination[start:ptr + 1]])
                    altActions.append(action)
                    alternate = walk(combination, ptr + 2, altActions, altTargets)
                if ptr < len(combination) - 2:
                    op = combination[ptr + 1]
                    nextDigit = int(combination[ptr + 2])
                    if op == '+':
                        total = total + nextDigit
                    elif op == '-':
                        total = total - nextDigit
                    else:
                        total = total * nextDigit
                ptr += 2
            leftovers = ifilter(lambda x: x not in ['+', '-', '*'], combination[start:])
            result = Result(actions, list(leftovers), targets)
            if alternate is not None and alternate.score() > result.score():
                return alternate
            return result

        return walk(self.combination, 0, [], self.targets)

# via http://stackoverflow.com/a/7947461/19794
def interleave(a, b):
    c = a + b
    c[::2] = a
    c[1::2] = b
    return c

digits = list(int(n) for n in inputs)
perms = set(permutations(digits, len(digits)))
ops = set(product(*repeat('-+*', len(digits) - 1)))

c = 0
winner = None
for p in perms:
    for op in ops:
        attempt = Attempt(interleave(list(p), list(op)), targets)
        result = attempt.run()
        if winner is None or winner.score() < result.score():
            winner = result
        if winner.solved() is True:
            break
        c += 1
        if c % 250000 == 0:
            print str(c) + " options processed"
    if winner.solved() is True:
        break
print winner
