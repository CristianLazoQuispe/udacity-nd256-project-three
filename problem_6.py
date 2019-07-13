class EmptyList(Exception):
    pass


class UdacityLies(Exception):
    pass


def get_min_max(ints):
    """
    Return a tuple(min, max) from the given list of unsorted integers (0-9)

    Args:
    ints(list): list of integers containing one or more integers

    :param ints: list
    :return: tuple
    """
    if len(ints) == 0:
        raise EmptyList

    current_min = 9
    current_max = 0

    for number in ints:
        if number < 0 or number > 9:
            raise UdacityLies
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
assert get_min_max([5]) == (5, 5)

try:
    get_min_max([0, -1])
    assert False, 'You promised the list would only contain the integers 0-9, Udacity'
except UdacityLies:
    assert True

try:
    get_min_max([0, 10])
    assert False, 'You promised the list would only contain the integers 0-9, Udacity'
except UdacityLies:
    assert True

try:
    get_min_max([])
    assert False, 'Cannot find the minimum and maximum values in an empty list'
except EmptyList:
    assert True
