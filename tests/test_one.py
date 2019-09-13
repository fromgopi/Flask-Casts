import pytest
import math


@pytest.fixture
def input_value():
    input = 40
    return input


def test_divisible_by_3(input_value):
    assert input_value % 3 != 0


def test_divisible_by_4(input_value):
    assert input_value % 4 == 0


def test_square(input_value):
    assert input_value * input_value == 1600
