import pytest

# hello

@pytest.mark.parametrize("i", range(52))
def test_num(i):
    if i in (17, 25):
        pytest.fail("bad luck")
