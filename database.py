import sqlite3
def get_db(): return sqlite3.connect('billing.db', check_same_thread=False)
