# Search in a rotated sorted array #
The submission contains two solutions to problem 2 (`problem_2.py` and `problem_2_alt.py`).

`problem_2.py` uses a modified binary search. `problem_2_alt.py` uses a self-balancing binary tree. Both work, but the binary search is preferred.

## Efficiency ##

### Time efficiency ###
The time efficiency of both solutions is `O(log(n))`.

### Space efficiency ###
The space efficiency of the binary search approach is `O(log(n))`. The space efficiency of the red-black tree approach is `O(n)`.

Both solutions use recursion, which requires space on the call stack for each recursive function call.
