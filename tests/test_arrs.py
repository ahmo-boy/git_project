import pytest
from utils.arrs import get, my_slice


def test_get_existing_index():
    array = [1, 2, 3, 4, 5]
    assert get(array, 2) == 3

def test_get_non_existing_index():
    array = [1, 2, 3, 4, 5]
    assert get(array, 10) is None

def test_get_with_default():
    array = [1, 2, 3, 4, 5]
    assert get(array, 10, "default") == "default"

def test_my_slice_without_arguments():
    coll = [1, 2, 3, 4, 5]
    assert my_slice(coll) == [1, 2, 3, 4, 5]

def test_my_slice_with_start():
    coll = [1, 2, 3, 4, 5]
    assert my_slice(coll, 2) == [3, 4, 5]

def test_my_slice_with_negative_start():
    coll = [1, 2, 3, 4, 5]
    assert my_slice(coll, -3) == [3, 4, 5]

def test_my_slice_with_end():
    coll = [1, 2, 3, 4, 5]
    assert my_slice(coll, end=3) == [1, 2, 3]

def test_my_slice_with_negative_end():
    coll = [1, 2, 3, 4, 5]
    assert my_slice(coll, end=-2) == [1, 2, 3]

def test_my_slice_with_start_and_end():
    coll = [1, 2, 3, 4, 5]
    assert my_slice(coll, 1, 4) == [2, 3, 4]

def test_my_slice_with_negative_start_and_end():
    coll = [1, 2, 3, 4, 5]
    assert my_slice(coll, -4, -1) == [2, 3, 4]

def test_my_slice_with_invalid_arguments():
    coll = [1, 2, 3, 4, 5]
    assert my_slice(coll, 10, 20) == []

def test_my_slice_with_start_greater_than_length():
    coll = [1, 2, 3, 4, 5]
    assert my_slice(coll, 10) == []

def test_my_slice_with_end_less_than_or_equal_to_zero():
    coll = [1, 2, 3, 4, 5]
    assert my_slice(coll, end=0) == []
    assert my_slice(coll, end=-1) == coll

def test_my_slice_with_zero_start_and_minus_one_end():
    coll = [1, 2, 3, 4, 5]
    assert my_slice(coll, 0, -1) == [1, 2, 3, 4]
