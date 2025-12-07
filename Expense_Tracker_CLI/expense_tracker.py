#!/usr/bin/env python3
import sqlite3
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

DB_FILE = "expenses.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        type TEXT NOT NULL CHECK(type IN ('income','expense')),
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        note TEXT
    )""")
    conn.commit()
    conn.close()

def add_entry(date_str, typ, category, amount, note=""):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO entries (date,type,category,amount,note) VALUES (?,?,?,?,?)",
              (date_str, typ, category, amount, note))
    conn.commit()
    conn.close()

def list_entries():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM entries ORDER BY date DESC")
    rows = c.fetchall()
    conn.close()
    return rows

def export_csv(path):
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query("SELECT * FROM entries", conn)
    df.to_csv(path, index=False)
    conn.close()

print("Expense Tracker CLI — Source Code")
