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
    ("DS3a1b1", False),
    ("AL1a2b3c5", True)
])
def test_validate_design(data, expected, store):
    """
    Parameterize test cases to check positive and negative test case for design generation after validation
    """
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


# Test for business logic
def test_positive_check_bouquet(store):
    """
    Case: Bouquet string should be pop from check_bouquet function
    """
    d = Design(name='A', size='S', species={'a': 2, 'b': 3}, total='3')
    store.list_of_designs = [d]
    store.flower_bucket['S'] = {'a': 2, 'b': 1}
    assert store.check_bouquet('S') == ['AS2a1b']


def test_negative_check_bouquet_n(store):
    """
    Case: Bouquet string should not be pop from check_bouquet function, empty list should be returned
    """
    d = Design(name='A', size='S', species={'a': 2, 'b': 3}, total='3')
    store.list_of_designs = [d]
    store.flower_bucket['S'] = {'a': 2, 'c': 1}
    assert store.check_bouquet('S') == []


# Tests for output
@pytest.mark.parametrize("data, expected", [
    (('A', 'L', {'a': 1, 'c': 2, 'b': 2}), 'AL1a2b2c'),
    (('A', 'S', {'a': 4, 'c': 3, 'b': 6, 'z': 7}), 'AS4a6b3c7z')
])
def test_prepare_bouquet(data, expected, store):
    """
    Test bouquet is prepared as per provided design
    """
    assert store.prepare_bouquet(*data) == expected
