import pytest

from .cli import generate_design


@pytest.mark.parametrize("data, expected", [
    ("ALa2b1100", False),
    ("al1a2b3", False),
    ("AL2a2b10", False),
    ("AL1a2b3c5", True)
])
def test_validate_design(data, expected):
    assert bool(generate_design(data)) == expected
