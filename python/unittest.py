from fizzbuzz import fizzbuzz
import unittest

def test_15():
    output = fizzbuzz(15)
    assert output,"fizzbuzz"
def test_3():
    output = fizzbuzz(3)
    assert output,"fizz"
def test_5():
    output = fizzbuzz(5)
    assert output,"buzz"