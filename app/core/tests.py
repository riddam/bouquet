import pytest
from .store import Store
from .design import Design


# Test setup
@pytest.fixture
def store():
    yield Store()


# Tests for input
@pytest.mark.parametrize("data, expected", [
    ("aS", True),
    ("sK", False),
    ("ssL", False),
    ("L", False)
])
def test_validate_flower(store, data, expected):
    assert store.validate_flower(data) == expected


@pytest.mark.parametrize("data, expected", [
    ("ALa2b1100", False),
    ("al1a2b3", False),
    ("AL2a2b10", False),
    ("AL1a2b3c5", True)
])
def test_validate_design(data, expected, store):
    assert bool(store.generate_design(data)) == expected


def test_validate_design_object(store):
    """
    Positive Case: Design object is created if valid design is provided
    """
    obj = store.generate_design("AL1a2b3c5")
    assert obj.name == "A"
    assert obj.size == "L"
    assert obj.total == 5
    assert obj.species["a"] == 1
    assert obj.species["b"] == 2
    assert obj.species["c"] == 3
