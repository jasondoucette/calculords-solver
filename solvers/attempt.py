from itertools import ifilter
import string
from result import Result

class Attempt(object):
    def __init__(self, source, combination, targets):
        self.source = source
        self.combination = combination
        self.targets = list(targets)
        self.all = string.maketrans('', '')
        self.nodigits = self.all.translate(self.all, string.digits)

    def run(self):
        def walk(combination, ptr, actionsSoFar, remainingTargets):
            start = ptr
            targets = list(remainingTargets)
            actions = list(actionsSoFar)
            if ptr >= len(combination):
                return Result(self.source, actions, [], targets)

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
            leftovers = str(combination[start:]).translate(self.all, self.nodigits)
            result = Result(self.source, actions, list(leftovers), targets)
            if alternate is not None and alternate.score() > result.score():
                return alternate
            return result

        return walk(self.combination, 0, [], self.targets)
