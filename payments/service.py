import uuid


def create_pro_subscription(tg_id: int) -> dict:
    """
    Временная заглушка оплаты.
    Потом заменим на YooKassa / Stripe.
    """

    fake_payment_id = str(uuid.uuid4())

    return {
        "payment_id": fake_payment_id,
        "pay_url": (
            "https://example.com/pay?"
            f"tg_id={tg_id}&payment_id={fake_payment_id}"
        ),
    }
