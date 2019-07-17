def sqrt(number):
    """
    Find the square root of the given number

    If the square root is not an integer, the next lowest integer is returned. If the square root cannot be determined,
    None is returned.

    :param number: The square
    :return: int or None
    """

    def recurse(candidates, target):
        if not candidates:
            return None

        mid_index = len(candidates) // 2
        candidate = candidates[mid_index]
        sq_candidate = candidate * candidate

        if sq_candidate == target:
            return candidate

        if sq_candidate < target:
            # If the next largest number squared is greater than the target, return the current candidate
            sq_candidate_plus = (candidate + 1) * (candidate + 1)
            if sq_candidate_plus > target:
                return candidate
            else:
                return recurse(candidates[mid_index + 1:], target)

        # We could just do an else: here, but let's be explicit
        if sq_candidate > target:
            return recurse(candidates[0:mid_index], target)

    # The answer can never be more than half the target number
    candidates = [x for x in range(0, (number // 2) + 2)]

    # Use a binary search to find the square root
    return recurse(candidates, number)


assert 1 == sqrt(1)
assert 2 == sqrt(4)
assert 3 == sqrt(9)
assert 1111 == sqrt(1_234_567)

# A non-integer answer should return the next lowest integer
assert 5 == sqrt(27)

# Edge cases
assert 0 == sqrt(0)
assert None is sqrt(-1)
