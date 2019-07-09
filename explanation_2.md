# Search in a rotated sorted array #
The submission contains two solutions to problem 2 (`problem_2.py` and `problem_2_alt.py`).

The "main" solution uses a modified binary search. The alternative approach uses a self-balancing binary tree, and is a much more complex solution (hence the "alt" suffix).

## Efficiency ##
The time efficiency of both solutions is `O(log(n))`. The space efficiency of the binary search approach is `O(1)`. The space efficiency of the red-black tree approach is `O(n)`.
