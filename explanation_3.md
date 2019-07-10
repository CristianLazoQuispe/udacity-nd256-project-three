# Rearrange array elements #
The solution involves two steps:

1. Sort the input list, in descending order. The sort method uses "merge sort" algorithm, to comply with the expected time complexity of `O(n log(n))`.
2. Loop through the sorted list, assigning elements with an odd index to `number_one`, and elements with an even index to `number_two`.

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
The time efficiency of the merge sort algorithm is `O(n log(n))`. The space efficiency is `O(n)`.
