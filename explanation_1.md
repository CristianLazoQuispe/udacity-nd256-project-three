# Finding the square root of an integer #
The solution uses the binary search algorithm to find the square root of a given number from a list of potential candidates.

## Details ##
Given a "target" number `n`, the `sqrt` function first creates a list containing all of the potential square root integers (the "candidates" list). The candidates list comprises all of the integers from `1` to `(n // 2) + 2`, inclusive.

The binary search is implemented using a recursive function. For each recursion, we check retrieve the value from the middle of the remaining candidates list. This is referred to as the `candidate` value. The result of `candidate * candidate` is checked against the target value.

- If the result equals the target value, our work is done.
- If the result is greater than the target value, we discard the bottom half of the candidates list, and recursively call the function with the new candidates.
- If the result is less than the target value, we perform an additional check, to determine whether `(candidate + 1) * (candidate + 1)` is _more than_ the target value. If it is, the square root must lay between `candidate` and `candidate + 1`. In this situation, we return `candidate`. If it is not, we discard the top half of the candidates list, and recursively call the function with the new candidates.

## Efficiency ##
The time efficiency of binary search (and therefore this solution) is `O(log(n))`. The space efficiency of this solution is `O(n / 2)`.
