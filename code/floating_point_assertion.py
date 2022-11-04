from numpy.testing import assert_allclose

def test_add_two_floats():
    # This assertion fails because of floating precission
    assert 0.1 + 0.2 = 0.3

def test_add_two_floats():
    # This succeeds because of absolute and relative tolerances
    assert_allclose(0.1 + 0.2, 0.3, atol=1e-5, rtol=1e-7)
