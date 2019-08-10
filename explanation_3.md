# Rearrange array elements #
The solution involves two steps:

1. Sort the input list, in descending order. The sort method uses "merge sort" algorithm, to comply with the expected time complexity of `O(n log(n))`.
2. Assign those elements from the sorted list with an odd index to the first number, and those with an even index to the second number.

## Why does this work? ##
By using the largest numbers from the input list as the most significant digits in the generated numbers, we are guaranteed to find the largest possible numbers.

For example:

```python
input_list = [1, 2, 3, 4, 5]
sorted_list = [5, 4, 3, 2, 1]

# Indices 0, 2, 4 from sorted_list
number_one = 531

# Indices 1, 3 from sorted list
number_two = 42
```

## Efficiency ##

### Time efficiency ###
The time efficiency of the merge sort algorithm is `O(n log(n))`.

### Space efficiency ###
The space efficiency is `O(n)`.

The solution first splits the original list, of length `n`, into two lists. The combined length of the two lists is `n`. It then uses the merge sort algorithm to combine the two lists into a single sorted list, again of length `n`.

Finally, two output strings are created from the sorted list. The combined length of the output strings is `n` characters.