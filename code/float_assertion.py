>>> x = [1e-5, 1e-3, 1e-1]
>>> y = np.arccos(np.cos(x))
>>> np.testing.assert_allclose(
...     x, y, rtol=1e-5, atol=0,
... )

>>> np.testing.assert_array_equal(
...     [1.0, 2.33333, np.nan],
...     [np.exp(0), 2.33333, np.nan],
... )
