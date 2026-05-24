import pandas as pd
import sqlite3

def load_data():
    # Load CSV
    df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month_name()

    # Save to SQLite database
    conn = sqlite3.connect("sales.db")
    df.to_sql("sales", conn, if_exists="replace", index=False)

    # Read back from SQL
    df = pd.read_sql("SELECT * FROM sales", conn)
    conn.close()
    return df