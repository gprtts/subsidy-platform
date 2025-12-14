from db.connection import get_connection


def get_alert_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT tg_id, business, region, industry
        FROM users
        WHERE alerts_enabled = TRUE
        """
    )
    rows = cur.fetchall()
    conn.close()
    return rows


def get_new_programs(last_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT id, title
        FROM programs
        WHERE id > %s
        """,
        (last_id,),
    )
    rows = cur.fetchall()
    conn.close()
    return rows
