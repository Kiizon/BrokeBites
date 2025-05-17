import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/frugalfeast')

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def get_dict_cursor(conn):
    return conn.cursor(cursor_factory=RealDictCursor)

