#!/usr/bin/env python

import sys
import argparse

from solvers.sampling import Sampling as SamplingSolver

parser = argparse.ArgumentParser(description='Solve Calculords rounds.')
parser.add_argument('inputs', type=int, help='input digits (concatenated as a string e.g. 12345678)')
parser.add_argument('target', type=int, nargs='+', help='target values to hit (space separated)')
args = parser.parse_args()

inputs = str(args.inputs)
targets = args.target

samplingSolver = SamplingSolver()
(result, c) = samplingSolver.solve(inputs, targets)
print "Solved in " + str(c) + "\n" + str(result)
