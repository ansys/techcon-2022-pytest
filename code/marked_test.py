from time import sleep
import pytest

@pytest.mark.slow
def test_a_very_slow_logic():
    sleep(10)

@pytest.mark.fast
def test_a_very_fast_test():
    ...
