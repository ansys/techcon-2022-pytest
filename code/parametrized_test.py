from numpy.testing import assert_allclose
import pytest

@pytest.mark.parametrize("a, b, c", [(0.1, 0.2, 0.3), (1.5, 2.3, 3.8)])
def test_add_two_floats(a, b, c):
    assert_allclose(a + b, c, atol=1e-5, rtol=1e-7)
