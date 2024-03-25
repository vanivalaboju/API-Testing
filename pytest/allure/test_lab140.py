# skip testcase in marked testcase meaning skipping testcase it is not ready yet to implement testcase
import pytest
def test_add():
    assert 2 + 2 == 0
@pytest.mark.smoke
def test_sub():
    assert 2 - 2 == 0
@pytest.mark.reg
def test_mul():
    assert 2 * 2 == 4

@pytest.mark.skip(reason="Not implemented yet")
def test_div():
        assert 4 / 2 == 2