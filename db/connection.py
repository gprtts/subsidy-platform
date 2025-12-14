import psycopg2
from core.settings import DATABASE_URL

def get_connection():
    return psycopg2.connect(DATABASE_URL)
