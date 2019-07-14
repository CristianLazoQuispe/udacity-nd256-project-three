# Search in a rotated sorted array #
The submission contains two solutions to problem 2 (`problem_2.py` and `problem_2_alt.py`).

`problem_2.py` uses a modified binary search. `problem_2_alt.py` uses a self-balancing binary tree. Both work, but the binary search is preferred.

## Efficiency ##
The time efficiency of both solutions is `O(log(n))`.

The space efficiency of the binary search approach is `O(1)`. The space efficiency of the red-black tree approach is `O(n)`.
