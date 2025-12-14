class PaymentProvider:
    def create_payment(self, user_id: int, amount: int, description: str):
        raise NotImplementedError
