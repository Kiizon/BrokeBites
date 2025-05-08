from database import get_connection

def upsert_postal_code(conn, postal_code):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO postal_codes (code)
            VALUES (%s)
            ON CONFLICT (code) DO UPDATE
            SET queried_at = NOW()
        """, (postal_code,))
    conn.commit()

def upsert_flyer(conn, flyer_id, store, date):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO flyers (id, store, flyer_date)
            VALUES (%s, %s, %s)
            ON CONFLICT (id) DO UPDATE
            SET store = EXCLUDED.store,
                flyer_date = EXCLUDED.flyer_date
        """, (flyer_id, store, date))
    conn.commit()

def link_flyer_to_postal(conn, postal_code, flyer_id):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO postal_code_flyers (postal_code, flyer_id)
            VALUES (%s, %s)
            ON CONFLICT DO NOTHING
        """, (postal_code, flyer_id))
    conn.commit()

def insert_sale_items(conn, flyer_id, items):
    with conn.cursor() as cur:
        for item in items:
            cur.execute("""
                INSERT INTO sale_items (flyer_id, name, sale_price)
                VALUES (%s, %s, %s)
            """, (flyer_id, item.get("name"), item.get("price")))
    conn.commit() 