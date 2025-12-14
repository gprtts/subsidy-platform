from db.connection import get_connection

def run():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO programs (region_code, title, description, amount, source_url)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        "77",
        "Тестовая субсидия Москвы",
        "Это тестовая запись для проверки пайплайна",
        "до 5 000 000 ₽",
        "https://mos.ru"
    ))

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Test program inserted")

if __name__ == "__main__":
    run()
