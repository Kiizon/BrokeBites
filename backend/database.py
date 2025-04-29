import sqlite3
conn = sqlite3.connect('broke_bites.db')
c = conn.cursor()

c.execute('''
  CREATE TABLE IF NOT EXISTS deals (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          item_name TEXT NOT NULL,
          price REAL,
          store_name TEXT
          )
'''
)


def insert_deal(item_name,price,store_name):
  conn = sqlite3.connect('broke_bites.db')
  c = conn.cursor()
  c.execute('INSERT INTO deals (item_name, price, store_name) VALUES (?,?,?)', (item_name, price, store_name))

  conn.commit()
  conn.close()

def fetch_all_deals():
  conn = sqlite3.connect('broke_bites.db')
  c = conn.cursor()
  c.execute('SELECT item_name, price, store_name FROM deals')
  results = c.fetchall()
  conn.close()
  return results

def clear_deals():
  conn = sqlite3.connect('broke_bites.db')
  c = conn.cursor()
  c.execute('DELETE FROM deals')
  conn.commit()
  conn.close()
  
if __name__ == "__main__":
  deals = fetch_all_deals()
  for deal in deals:
      print(deal)
