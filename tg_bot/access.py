from db.connection import get_connection

FREE_LIMIT = 3


def check_access(tg_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT free_requests, is_pro FROM users WHERE tg_id = %s",
        (tg_id,),
    )
    row = cur.fetchone()
    conn.close()

    if not row:
        return False, "Пользователь не найден"

    free_requests, is_pro = row

    if is_pro:
        return True, ""

    if free_requests <= 0:
        return False, (
            "❌ Лимит бесплатных запросов исчерпан.\n\n"
            "Оформи подписку, чтобы получать новые субсидии автоматически."
        )

    return True, ""


def consume_request(tg_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE users
        SET free_requests = free_requests - 1
        WHERE tg_id = %s AND free_requests > 0
        """,
        (tg_id,),
    )
    conn.commit()
    conn.close()
