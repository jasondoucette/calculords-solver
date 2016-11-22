# Calculords Solver

Simple script to calculate optimal plays for the game
[Calculords](http://www.calculords.com/)

Rather than calculate all the possible play permutations, the script plays
randomly a given number of times and then returns the best result found.

## Usage

At the moment gameplay is managed via direct edits to the source code (so,
yeah, TODO.)  Edit the `inputs` and `targets` variables at the top of the
file and run the script. Then play the actions. Repeat until enemy base
is captured :)

## Possibly unsolvable cases:

The following cases failed to clear completely in testing, but I haven't tried
to solve them manually yet (in these scenarios, the goal is to have zero
targets remaining.)

 - inputs = `[6,1,8,4,3,4,7,3]`, targets = `[20,100,62]`
 - inputs = `[8,1,5,4,8,4,7,7]`, targets = `[58,10,27]`
 - inputs = `[4,8,4,9,7,3,3,6]`, targets = `[28,35,63]`

This isn't necessarily a bug, just an indicator that there might be
room for optimization.
