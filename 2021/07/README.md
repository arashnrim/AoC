# 💥 Difficulty encountered

## Problem

I experienced issues with this day's task due to **performance issues**. The solution in `part2.py` works, but a result cannot be produced because of the inefficiency of the source code by normal means <sup>(see below)</sup>.

Taking a look at my solution in `part2.py`, a nested for loop is utilised in order to loop through every value in the `timers` list for 80 iterations.

```python
for potentialOutcome in range(max(positions)):
    total = []
    for position in positions:
        count, value, variablePosition = 1, 0, position
        while variablePosition != potentialOutcome:
            value += count
            variablePosition += 1 if variablePosition < potentialOutcome else -1
            count += 1
        total.append(value)
    possibilities.append(sum(total))
```

This gives a Big-O complexity of O(n<sup>2</sup>), which can be seen as an extremely inefficient. Additionally, given that Python isn't an extremely fast language, the calculation required for part 2 will take an extremely long time.

## Attempted solutions

I am still looking into possible solutions for this matter, including:

- [x] trying to use [PyPy](https://pypy.org)

## Solution

PyPy was able to significantly reduce the time taken for the program to complete. Even so, however, I found the execution to be rather disappointing — if I have the time and knowledge to figure out a more optimised method to solving the problem, I'll try to implement it!

I'd consider this a quasi-pass on my end; although the code is able to produce a result given some time, the performance of it is unsatisfactory.
