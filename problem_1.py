def sqrt(number):
    """
    Find the square root of the given number

    If the square root is not an integer, the next lowest integer is returned. If the square root cannot be determined,
    None is returned.

    :param number: The square
    :return: int or None
    """

    # Explicitly handle the edge-cases here
    if number < 0:
        return None
    if number <= 1:
        return number

    lowest, highest = 0, number // 2

    while lowest <= highest:
        candidate = ((highest - lowest) // 2) + lowest
        sq_candidate = candidate * candidate

        if sq_candidate == number:
            return candidate

        if sq_candidate > number:
            highest = candidate - 1
        else:
            # If the next largest number squared is greater than the target, return the current candidate
            sq_candidate_plus = (candidate + 1) * (candidate + 1)
            if sq_candidate_plus > number:
                return candidate
            lowest = candidate + 1

    # If we got this far, all hope is lost
    return None


assert 2 == sqrt(4)
assert 3 == sqrt(9)
assert 1111 == sqrt(1_234_567)

# A non-integer answer should return the next lowest integer
assert 5 == sqrt(27)

# Edge cases
assert None is sqrt(-1)
assert 0 == sqrt(0)
assert 1 == sqrt(1)
