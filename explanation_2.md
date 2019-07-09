# Search in a rotated sorted array #
The solution uses a self-balancing binary tree to search a rotated sorted array of values.

## Efficiency ##
The problem states that the search function must have a time-efficiency of `O(log(n))`. This rules out a standard binary tree, whose worst-case time efficiency is `O(n)`.

However, searching a _self-balancing_ binary tree (or "red black" tree) has the desired time-efficiency of `O(log(n))`.

The space efficiency of the solution is `O(n)`.
