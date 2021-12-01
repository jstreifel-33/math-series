from math_series.series import fibonacci, lucas, sum_series
import pytest

#Deco for skipping tests:
#@pytest.mark.skip("pending")

# Fibonacci tests

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

# Lucas tests

def test_import_lucas():
  assert lucas

def test_lucas_0():
  actual = lucas(0)
  expected = 2
  assert actual == expected