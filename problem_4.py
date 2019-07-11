def sort_012(input_list):
    """
    Sort a list containing the integers 0, 1, and 2, in a single traversal

    :param input_list: list
    :return: list
    """
    current_index = 0
    zero_index = 0
    two_index = len(input_list) - 1

    while current_index <= two_index:
        if input_list[current_index] is 2:
            input_list[current_index], input_list[two_index] = input_list[two_index], input_list[current_index]
            two_index -= 1
            continue

        if input_list[current_index] is 0:
            input_list[current_index], input_list[zero_index] = input_list[zero_index], input_list[current_index]
            zero_index += 1

        current_index += 1

    return input_list


# ----------------------------------------------------------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------------------------------------------------------
assert sort_012([0, 1, 2]) == [0, 1, 2]
assert sort_012([2, 1, 0]) == [0, 1, 2]
assert sort_012([0, 1, 0]) == [0, 0, 1]
assert sort_012([0, 2, 0]) == [0, 0, 2]
assert sort_012([1, 2, 1]) == [1, 1, 2]
assert sort_012([2, 2, 1, 1, 0, 0]) == [0, 0, 1, 1, 2, 2]
assert sort_012([2, 1, 0, 2, 1, 0]) == [0, 0, 1, 1, 2, 2]
assert sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]) == [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

assert sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) == [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1,
    2, 2, 2, 2, 2, 2, 2, 2, 2
    ]

assert sort_012([]) == []
