class EmptyList(Exception):
    pass


class InvalidValue(Exception):
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

    if not input_list:
        raise EmptyList

    sorted_list = sort(input_list)
    number_one = '0'
    number_two = '0'

    for index in range(len(sorted_list)):
        if sorted_list[index] < 0:
            raise InvalidValue

        digit_string = str(sorted_list[index])

        if index % 2 == 0:
            number_one += digit_string
        else:
            number_two += digit_string

    return int(number_one), int(number_two)


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
assert rearrange_digits([1]) == (1, 0)

try:
    rearrange_digits([])
    assert False, 'Cannot rearrange digits in an empty list'
except EmptyList:
    assert True

try:
    rearrange_digits([1, 2, 3, 4, -1])
    assert False, 'All digits must be in the range 0-9'
except InvalidValue:
    assert True
