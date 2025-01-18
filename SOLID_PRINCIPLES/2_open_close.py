"""O: Open/Closed Principle (OCP)

Definition:
    A class should be opend to extension but closed to modification.

Tip:
    You can achieve this by using abstract classes and interfaces.

Advantages:
    - Makes your code more modular and easier to maintain.
    - Reduces the risk of breaking existing code.
    - Makes your code more testable.
"""

############################################
# Bad example:
############################################

class MakePayment:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def pay(self):
        if self.payment_method == 'credit_card':
            print('Paying using credit card')
        elif self.payment_method == 'paypal':
            print('Paying using PayPal')
        else:
            raise ValueError('Unknown payment method')

# WHy this is bad in terms of OCP?
# If we want to add a new payment method (say, Bitcoin), we have to modify the class.
# This violates the OCP principle.

############################################
# Good example:
############################################

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self):
        raise NotImplementedError  # This method should be implemented in the child classes


class CreditCardPayment(Payment):
    def pay(self):
        print('Paying using credit card')


class PaypalPayment(Payment):
    def pay(self):
        print('Paying using PayPal')


class BitcoinPayment(Payment):
    def pay(self):
        print('Paying using Bitcoin')
