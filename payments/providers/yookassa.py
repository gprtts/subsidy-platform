from payments.providers.base import PaymentProvider
import uuid

class YooKassaProvider(PaymentProvider):
    def create_payment(self, user_id: int, amount: int, description: str):
        payment_id = str(uuid.uuid4())

        return {
            "payment_id": payment_id,
            "pay_url": f"https://pay.yookassa.ru/mock/{payment_id}"
        }
