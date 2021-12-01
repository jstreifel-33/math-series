def confirm_ints(*things):
    for thing in things:
        if isinstance(thing, bool) or not isinstance(thing, int):
            return False

    return True


def fibonacci(n):
    """
    Returns 'nth' number in the Fibonacci
    sequence. (0, 1, 1, 2, 3, 5, ...)
    """

    if confirm_ints(n) == False:
        return 'Function only accepts integers!'

    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    Returns 'nth' number in the Lucas sequence.
    Similar to Fibonacci, but starts with 2 and 1.
    (2, 1, 3, 4, 7, 11, 18, ...)
    """
    if confirm_ints(n) == False:
        return 'Function only accepts integers!'

    if n == 0:
        return 2
    elif n == 1:
        return 1

    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, i=0, j=1):
    """
    Returns 'nth' number in any sum sequence,
    given a first and second argument.
    (i, j, i+j, i+2j, 2i+3j, ...)
    """
    if confirm_ints(n, j, i) == False:
        return 'Function only accepts integers!'

    if n == 0:
        return i
    elif n == 1:
        return j

    return sum_series(n - 1, i, j) + sum_series(n - 2, i, j)
