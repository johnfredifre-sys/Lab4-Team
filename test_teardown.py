import pytest


@pytest.fixture
def setup_and_teardown():
    print("\n[setup]")

    yield

    print("[teardown]")


def test_first(setup_and_teardown):
    print("Running first test")
    assert True


def test_second(setup_and_teardown):
    print("Running second test")
    assert True