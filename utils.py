import pandas as pd

def load_data():
    df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")  # ← add encoding
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month_name()
    return df