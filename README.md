# Calculords Solver

Simple scripts to calculate optimal plays for the game
[Calculords](http://www.calculords.com/)

There are two different solvers here:

`exhaustive.py` will check all possible combinations, exiting only when a
perfect solution (no remaining inputs or targets) is found or all options
have been tried.

`sampling.py` will run 100,000 randomly selected combinations and return
the best one found.

Rather than calculate all the possible play permutations, the script plays
randomly a given number of times and then returns the best result found.

## Usage

At the moment gameplay is managed via direct edits to the source code (so,
yeah, TODO.)  Edit the `inputs` and `targets` variables at the top of the
file and run the script. Then play the actions. Repeat until enemy base
is captured :)

## Unsolvable cases:

For reference, the following cases failed to clear completely via either
solver (there are many others of course, but these have been used for
validation.)

The difference between solvers is readily apparent here: while the sampling
solver will return in relatively constant time (around 5s on a MacBook Air,)
the exhaustive solver will take 9.5 minutes to come to the same conclusion.

 - inputs = `[6,1,8,4,3,4,7,3]`, targets = `[20,100,62]`
 - inputs = `[8,1,5,4,8,4,7,7]`, targets = `[58,10,27]`
 - inputs = `[4,8,4,9,7,3,3,6]`, targets = `[28,35,63]`
