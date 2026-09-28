import pytest


@pytest.fixture
def resource():
    print("[setup]")
    yield
    print("[teardown]")


def test_first(resource):
    print("running test_first")
    assert 1 + 1 == 2


def test_second(resource):
    print("running test_second")
    assert "abc".upper() == "ABC"