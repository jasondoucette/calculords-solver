#!/usr/bin/env python

from itertools import permutations
import random

cycles = 100000
# Inputs are single digit so use a string list for faster data entry...
inputs = list(int(n) for n in list("15968764"))
targets = [48,10,12]

class Attempt(object):

    def __init__(self, inputs, target):
        self.inputs = list(inputs)
        self.inputCount = len(inputs)
        self.targets = list(targets)
        self.targetCount = len(targets)
        self.originalTargets = sorted(targets)
        self.operations = ['-', '+', '*']
        self.actions = []
        self.score = 0

        self.run()

    def __str__(self):
        return "Score: {}\nLeftover inputs: {}\nLeftover targets: {}\nActions:\n  {}\n\n".format(
            str(self.score),
            ", ".join(str(i) for i in sorted(self.inputs)),
            ", ".join(str(i) for i in sorted(self.targets)),
            "\n  ".join(self.actions))

    def sample(self, data, keep = False):
        if len(data) == 0:
            return None
        result = random.choice(data)
        if keep == False:
            data.remove(result)
        return result

    def calcScore(self):
        if len(self.targets) > 3:
            self.score == 0
        else:
            # Fewer targets is better than more targets:
            targetScore = 10*(self.targetCount-len(self.targets))
            # Fewer high targets is better than fewer low targets:
            targetScore += sum(3*(self.targetCount - 1 - self.originalTargets.index(n)) for n in self.targets)
            # Prioritize fewer leftover inputs:
            inputScore = (self.inputCount-len(self.inputs))
            self.score = targetScore + inputScore


    def run(self):
        output = None
        action = ''
        while len(self.inputs) > 0:
            if output is None:
                output = self.sample(self.inputs)
                action = str(output)
            while output not in self.targets and len(self.inputs) > 0:
                operation = self.sample(self.operations, True)
                nextNumber = self.sample(self.inputs)
                if nextNumber is not None:
                    action += operation + str(nextNumber)
                    if operation == '-':
                        output = output - nextNumber
                    elif operation == '+':
                        output = output + nextNumber
                    else:
                        output = output * nextNumber
            if output in self.targets:
                # if we have a match but there are larger possible targets
                # yet to be hit, keep going a certain percentage of the time.
                if max(self.targets) == output or random.randint(1, 3) == 1:
                    self.targets.remove(output)
                    self.actions.append(action)
                    output = None
        if len(self.actions) == 0 or self.actions[-1] != action:
            # undo the last failed attempt
            for char in action:
                if char not in self.operations:
                    self.inputs.append(int(char))
        self.calcScore()

winner = None
for n in range(cycles):
    attempt = Attempt(inputs, targets)
    if winner is None or attempt.score > winner.score:
        winner = attempt
print winner
