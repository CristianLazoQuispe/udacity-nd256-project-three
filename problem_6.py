class EmptyList(Exception):
    pass


def get_min_max(ints):
    """
    Return a tuple(min, max) from the given list of unsorted integers

    Args:
    ints(list): list of integers containing one or more integers

    :param ints: list
    :return: tuple
    """
    if len(ints) == 0:
        raise EmptyList

    current_min = current_max = ints[0]

    for number in ints[1:]:
        if number < current_min:
            current_min = number
        if number > current_max:
            current_max = number

    return current_min, current_max


# ----------------------------------------------------------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------------------------------------------------------
assert get_min_max([0, 1]) == (0, 1)
assert get_min_max([1, 0]) == (0, 1)
assert get_min_max([5, 3, 2, 1, 9, 0, 7]) == (0, 9)
assert get_min_max([-2, -1, 0, 1, 2]) == (-2, 2)
assert get_min_max([5]) == (5, 5)

try:
    get_min_max([])
    assert False, 'Cannot find the minimum and maximum values in an empty list'
except EmptyList:
    assert True
