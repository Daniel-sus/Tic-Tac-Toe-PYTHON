import pytest

# Step 1: Write Test
def test_bank_account():
    # Test deposit method with positive amount
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100

    # Test deposit method with zero amount
    with pytest.raises(ValueError):
        account.deposit(0)

    # Test deposit method with negative amount
    with pytest.raises(ValueError):
        account.deposit(-50)

    # Test withdraw method
    account.withdraw(50)
    assert account.get_balance() == 50

    # Test withdraw with insufficient funds
    with pytest.raises(ValueError):
        account.withdraw(200)

    # Test overdraft feature
    account.set_overdraft(200)
    assert account.get_overdraft() == 200

    # Test balance and available funds
    account.deposit(100)
    assert account.get_balance() == 150
    assert account.get_available_funds() == 350  # Balance (150) + Overdraft (200)


# Step 3: Write Code
class BankAccount:
    def __init__(self):
        self.balance = 0
        self.overdraft = 100  # Default overdraft of 100

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.get_available_funds() < amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def set_overdraft(self, amount):
        if amount < 0:
            raise ValueError("Overdraft amount cannot be negative")
        self.overdraft = amount

    def get_overdraft(self):
        return self.overdraft

    def get_available_funds(self):
        return self.balance + self.overdraft
