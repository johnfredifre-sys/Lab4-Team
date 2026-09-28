import pytest
from bank import BankAccount


@pytest.fixture
def account():
    """Create a fresh bank account with an initial balance of 100."""
    return BankAccount(100)


def test_deposit_multiple_times(account):
    """Verify that multiple deposits correctly update the balance."""

    account.deposit(50)
    assert account.balance == 150

    account.deposit(25)
    assert account.balance == 175

    account.deposit(75)
    assert account.balance == 250


def test_deposit_different_amounts(account):
    """Verify deposits of different amounts from the initial balance."""

    initial_balance = account.balance

    account.deposit(10)
    assert account.balance == initial_balance + 10

    account.deposit(40)
    assert account.balance == initial_balance + 50
