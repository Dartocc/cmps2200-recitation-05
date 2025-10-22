# Test file needed for autograder?
from main import *
import random

def test_ssort():
    L = [5, 3, 2, 4, 1]
    assert ssort(L) == [1, 2, 3, 4, 5]

def test_qsort_fixed():
    assert qsort([5, 4, 3, 2, 1], lambda a: a[0]) == [1, 2, 3, 4, 5]

def test_qsort_random():
    random.seed(0)
    assert qsort([5, 4, 3, 2, 1], lambda a: random.choice(a)) == [1, 2, 3, 4, 5]
