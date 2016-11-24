#!/usr/bin/env python

import time
from multiprocessing import Process, Pipe
from solvers.sampling import Sampling as SamplingSolver
from solvers.exhaustive import Exhaustive as ExhaustiveSolver

inputs = '15968764'
targets = [48,10,12]

def worker(conn, solver, inputs, targets):
    conn.send(str(solver.solve(inputs, targets)))

samplingSolver = SamplingSolver()
exhaustiveSolver = ExhaustiveSolver()

processes = []
parentConn, childConn = Pipe()
for solver in [samplingSolver, exhaustiveSolver]:
    p = Process(
        target = worker,
        args = (childConn, solver, inputs, targets))
    p.start()
    processes.append(p)

# Block until we get a response from one of the solvers
print parentConn.recv()

# Now kill the rest of them
for p in processes:
    if p.is_alive():
        p.terminate()
    p.join()

