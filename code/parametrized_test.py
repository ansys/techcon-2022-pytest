from numpy.testing import assert_allclose
import pytest

@pytest.mark.parametrize(
    "a, b, c",
    [(0.1, 0.2, 0.3), (8, 12, 20)]
)
def test_add_two_floats(a, b, c):
    assert a + b == c
