from math_series.series import fibonacci, lucas, sum_series
import pytest

#Deco for skipping tests:
#@pytest.mark.skip("pending")

# fibonacci tests

def test_import_fibonacci():
  assert fibonacci

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

def test_import_lucas():
  assert lucas

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

def test_import_sum_series():
  assert sum_series

## variable n; default i, j

def test_sum_series_0():
  actual = sum_series(0)
  expected = 0
  assert actual == expected