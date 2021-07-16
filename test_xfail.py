import pytest

@pytest.mark.xfail(strict=True) #test_xfail.py::test_succeed FAILED
def test_succeed():
    assert True

@pytest.mark.xfail
def test_not_succeed():
    assert False

@pytest.mark.skip
def test_skipped():
    assert False