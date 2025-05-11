from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class PayPal(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing ${amount} via PayPal")

class MasterCard(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing ${amount} via MasterCard")

pay1=MasterCard()

pay1.process_payment(20)

pay2=PayPal()
pay2.process_payment(30)