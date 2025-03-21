import pytest
from plugins.sample_plugin import square

def test_square():
    result = square(3)
    assert result == 9

def test_square_negative():
    result = square(-3)
    assert result == 9

