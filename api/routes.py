from fastapi import APIRouter
from db.connection import get_connection

router = APIRouter()

@router.get("/programs")
def get_programs(region: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, region_code, title, description, amount, deadline, source_url
        FROM programs
        WHERE region_code = %s
        ORDER BY created_at DESC
        LIMIT 50
    """, (region,))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {
            "id": r[0],
            "region": r[1],
            "title": r[2],
            "description": r[3],
            "amount": r[4],
            "deadline": r[5],
            "url": r[6],
        }
        for r in rows
    ]
