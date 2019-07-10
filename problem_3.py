class InvalidList(Exception):
    pass


def merge(left_list, right_list):
    """
    Merge the given lists into a single list whose items are in descending order

    :param left_list: list
    :param right_list: list
    :return: list
    """

    merged_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            merged_list.append(right_list[right_index])
            right_index += 1
        else:
            merged_list.append(left_list[left_index])
            left_index += 1

    # Add any remaining elements to the merged list
    merged_list += left_list[left_index:]
    merged_list += right_list[right_index:]

    return merged_list


def sort(input_list):
    """
    Sort the given list in descending order

    :param input_list: list
    :return: list
    """
    if len(input_list) <= 1:
        return input_list

    mid_index = len(input_list) // 2
    left_list = sort(input_list[0:mid_index])
    right_list = sort(input_list[mid_index:])

    return merge(left_list, right_list)


def rearrange_digits(input_list):
    """
    Extract two numbers from the given array, whose sum is the maximum value possible using the available digits

    :param input_list: list
    :return: tuple
    """
    if len(input_list) <= 1:
        raise InvalidList

    sorted_list = sort(input_list)
    number_one_list = [str(x) for x in sorted_list[0::2] if x >= 0]
    number_two_list = [str(x) for x in sorted_list[1::2] if x >= 0]

    return int(''.join(number_one_list)), int(''.join(number_two_list))


# ----------------------------------------------------------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------------------------------------------------------
assert sort([5, 2, 4, 3, 1]) == [5, 4, 3, 2, 1]
assert sort([4, 4, 5, 5, -1]) == [5, 5, 4, 4, -1]

assert rearrange_digits([1, 2, 3, 4, 5]) == (531, 42)
assert rearrange_digits([1, 2, 3, 4, 5, 6]) == (642, 531)
assert rearrange_digits([4, 6, 2, 5, 9, 8]) == (964, 852)

assert rearrange_digits([1, 0, 1, 0]) == (10, 10)
assert rearrange_digits([0, 0, 0]) == (0, 0)

# Discard any digits less than zero. You said this would never happen, Udacity.
assert rearrange_digits([1, 2, 3, 4, -1]) == (42, 31)

try:
    rearrange_digits([])
    assert False, 'Cannot rearrange digits in an empty list'
except InvalidList:
    assert True

try:
    rearrange_digits([1])
    assert False, 'The list must contain at least two digits'
except InvalidList:
    assert True
