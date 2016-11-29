#!/usr/bin/env python

from solvers.sampling import Sampling as SamplingSolver
from solvers.exhaustive import Exhaustive as ExhaustiveSolver

inputs = '176485298'
targets = [6,12,112]

exhaustiveSolver = ExhaustiveSolver()
(result, c) = exhaustiveSolver.solve(inputs, targets)
if result is None:
    samplingSolver = SamplingSolver()
    (result, c) = samplingSolver.solve(inputs, targets)
print "Solved in " + str(c) + "\n" + str(result)
