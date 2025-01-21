"""Proxy Design Pattern Example."""
# The Proxy Design Pattern provides a surrogate or placeholder for another object to control access to it.
# This example demonstrates a simple ATM Proxy that controls access to a BankAccount object.
# The BankAccount class handles actual bank account operations, while the ATM class acts as a proxy to control access.
# The ATM proxy checks the user's PIN before allowing withdrawals or deposits on the bank account.

class BankAccount:
    """The Real Subject: Handles actual bank account operations."""

    def __init__(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"BankAccount: Withdrawal of ${amount} successful. Remaining balance: ${self._balance}.")
        else:
            print("BankAccount: Insufficient funds.")

    def deposit(self, amount):
        self._balance += amount
        print(f"BankAccount: Deposit of ${amount} successful. New balance: ${self._balance}.")


class ATM:
    """The Proxy: Controls access to the BankAccount."""

    def __init__(self, bank_account):
        self._bank_account = bank_account

    @staticmethod
    def authenticate(pin):
        # Simulate PIN authentication
        if pin == "1234":
            print("ATM: Authentication successful.")
            return True
        else:
            print("ATM: Invalid PIN. Access denied.")
            return False

    def withdraw(self, amount, pin):
        if self.authenticate(pin):
            self._bank_account.withdraw(amount)

    def deposit(self, amount, pin):
        if self.authenticate(pin):
            self._bank_account.deposit(amount)


# Example Usage
def main():
    print("Scenario: Using an ATM to access a bank account.")

    # Create a real bank account with a starting balance
    account = BankAccount(balance=1000)

    # Use an ATM proxy to interact with the bank account
    atm = ATM(bank_account=account)

    print("\nAttempting to withdraw with correct PIN:")
    atm.withdraw(amount=200, pin="1234")

    print("\nAttempting to withdraw with incorrect PIN:")
    atm.withdraw(amount=100, pin="5678")

    print("\nDepositing money with correct PIN:")
    atm.deposit(amount=300, pin="1234")


main()
