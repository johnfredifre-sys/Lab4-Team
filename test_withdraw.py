import pytest
from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount(100)


def test_withdraw_reduces_balance(account):
    result = account.withdraw(40)
    assert result == 60
    assert account.balance == 60