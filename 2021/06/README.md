# ⚠️ Incomplete solution

I am experiencing issues with this day's task due to **performance issues**. The solution in `part1.py` can be applied to `part2.py` as the logic has not changed between the parts, but a result cannot be produced because of the inefficiency of the source code.

## Details

Taking a look at my solution in `part1.py`, a nested for loop is utilised in order to loop through every value in the `timers` list for 80 iterations.

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

I am still looking into possible solutions for this matter, including trying faster programming languages (e.g., [Go](https://go.dev) and [C++](https://isocpp.org/)). It may take a while for me to be able to port my current solution into the other languages, though it may appear easy!

I'm also looking for ways to make my code better — if possible, reducing the complexity entirely to O(n).
