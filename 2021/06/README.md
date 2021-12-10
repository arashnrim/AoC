# 💥 Difficulty encountered

## Problem

I experienced issues with this day's task due to **performance issues**. The solution in `part1.py` can be applied to `part2.py` as the logic has not changed between the parts, but a result cannot be produced because of the inefficiency of the source code.

Taking a look at my solution in `oldSolution.py`, a nested for loop is utilised in order to loop through every value in the `timers` list for 80 iterations.

```python
for _ in range(80):
    new = 0
    for index, timer in enumerate(timers):
        if index > (len(timers) - new - 1):
            break
        timer -= 1
        if timer == -1:
            timers.append(8)
            new += 1
        timers[index] = 6 if timer == -1 else timer
```

This gives a Big-O complexity of O(n<sup>2</sup>), which can be seen as an extremely inefficient. Additionally, given that Python isn't an extremely fast language, the calculation required for part 2 will take an extremely long time — longer than 15 minutes, even.

## Attempted solutions

I am still looking into possible solutions for this matter, including:

- [ ] trying faster programming languages (e.g., [Go](https://go.dev) and [C++](https://isocpp.org/))
- [x] trying to use [NumPy](https://numpy.org)
- [x] trying to use [PyPy](https://pypy.org)
- [ ] reducing code complexity

## Solution

@Ninja9000 explained to me that there could be another way to view the problem; instead of having a list which dynamically changes its size, we can use a list which has a size that does not change — in other words, a list tracking the frequency of each timer.

For instance, taking the example input of `[3, 4, 3, 1, 2]`, I can create another list to keep track of the frequency of each timer — i.e., `[0, 1, 1, 2, 1, 0, 0, 0, 0]`.

That improves things significantly since the number of items that has to be iterated each loop doesn't change. This greatly improves performance and makes the code run faster — within less than a second!

I've learnt that there can be different ways to see a problem even if it appears easy at first. In some cases (like this), the different way is better than the easy way! Thank you and kudos for showing the way, @Ninja9000!
