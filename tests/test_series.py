from math_series.series import fibonacci, lucas, sum_series
import pytest

# Deco for skipping tests:
# @pytest.mark.skip("pending")

# fibonacci tests

## proof of import life


def test_import_fibonacci():
    assert fibonacci


## signature testing


def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_5():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_fibonacci_10():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


# lucas tests

## proof of import life


def test_import_lucas():
    assert lucas


## signature testing


def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_5():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_lucas_10():
    actual = lucas(10)
    expected = 123
    assert actual == expected


# sum_series tests

## proof of import life


def test_import_sum_series():
    assert sum_series


## signature testing

### variable n; default i, j


def test_sum_series_0():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sum_series_5():
    actual = sum_series(5)
    expected = 5
    assert actual == expected


### fixed n=5; variable i, j


def test_sum_series_as_fib():
    actual = sum_series(5, 0, 1)
    expected = 5
    assert actual == expected


def test_sum_series_as_lucas():
    actual = sum_series(5, 2, 1)
    expected = 11
    assert actual == expected


def test_sum_series_i3_j6():
    actual = sum_series(5, 3, 6)
    expected = 39
    assert actual == expected


### variable n, i, j


def test_sum_series_n3_i4_j5():
    actual = sum_series(3, 4, 5)
    expected = 14
    assert actual == expected


def test_sum_series_n5_i100_j123():
    actual = sum_series(5, 100, 123)
    expected = 915
    assert actual == expected


# edge cases

## input not an integer


def test_fibonacci_not_number():
    actual = fibonacci("string")
    expected = "Function only accepts integers!"
    assert actual == expected


def test_lucas_not_number():
    actual = lucas(True)
    expected = "Function only accepts integers!"
    assert actual == expected


def test_sum_series_not_number():
    actual = sum_series(3.14)
    expected = "Function only accepts integers!"
    assert actual == expected


def test_sum_series_not_number():
    actual = sum_series(0, "whee", 9)
    expected = "Function only accepts integers!"
    assert actual == expected


def test_sum_series_not_number():
    actual = sum_series(0, 9, False)
    expected = "Function only accepts integers!"
    assert actual == expected
