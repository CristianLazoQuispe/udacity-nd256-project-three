class EmptyHaystack(Exception):
    pass


def is_sorted(stack):
    return stack[0] < stack[-1] if len(stack) > 1 else True

def sorted_stack_contains_needle(stack, needle):
    if not stack:
        return False
    return stack[0] <= needle <= stack[-1]

def rotated_array_search(haystack, needle):
    """
    Find the given needle in the given haystack

    If the needle is found, return its index. If it cannot be found, return -1

    :param haystack: the list to search
    :param needle: the value to find
    :return: the value index, or -1
    """
    if not haystack:
        raise EmptyHaystack()

    start_index = 0

    while len(haystack) > 0:
        mid_index = len(haystack) // 2
        mid_value = haystack[mid_index]

        if mid_value == needle:
            return start_index + mid_index

        # One side of the haystack must be sorted. Figure out which.
        left_stack = haystack[0:mid_index]
        right_stack = haystack[mid_index + 1:]

        if is_sorted(left_stack) and sorted_stack_contains_needle(left_stack, needle):
            haystack = left_stack
        else:
            haystack = right_stack
            start_index = start_index + mid_index + 1

    return -1


# ----------------------------------------------------------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------------------------------------------------------
# Rotation point is the centre element
assert rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 7) == 1
assert rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 4) == 8

# Rotation point is to the left
assert rotated_array_search([8, 9, 10, 1, 2, 3, 4, 5, 6, 7], 6) == 8
assert rotated_array_search([8, 9, 10, 1, 2, 3, 4, 5, 6, 7], 3) == 5

# Rotation point is to the right
assert rotated_array_search([4, 5, 6, 7, 8, 9, 10, 1, 2, 3], 8) == 4
assert rotated_array_search([4, 5, 6, 7, 8, 9, 10, 1, 2, 3], 3) == 9

# Missing element
assert rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 0) == -1
assert rotated_array_search([4, 5, 6, 7, 8, 9, 10, 1, 2, 3], 0) == -1
assert rotated_array_search([8, 9, 10, 1, 2, 3, 4, 5, 6, 7], 0) == -1

try:
    rotated_array_search([], 12)
    assert False, 'Attempting to create an empty haystack should raise an EmptyHaystack exception'
except EmptyHaystack:
    assert True
