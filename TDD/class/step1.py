import pytest


# Step 1: Write Test
def test_bank_account():
    # Test deposit method with positive amount
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100

    # Test deposit method with zero amount
    account.deposit(0)
    assert account.get_balance() == 100

    # Test deposit method with negative amount
    with pytest.raises(ValueError):
        account.deposit(-50)

    # Test withdraw method
    account.withdraw(50)
    assert account.get_balance() == 50

    # Test withdraw with insufficient funds
    with pytest.raises(ValueError):
        account.withdraw(100)
