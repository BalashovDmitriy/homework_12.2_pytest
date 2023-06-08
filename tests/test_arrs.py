import pytest

from utils import arrs


@pytest.fixture
def data():
    return [1, 2, 3]


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(data):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(data, 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(data, -1) == [3]
    assert arrs.my_slice(data, -5) == [1, 2, 3]
