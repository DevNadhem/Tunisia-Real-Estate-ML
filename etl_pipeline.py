import pandas as pd
import sqlite3

def run_etl():
    # 1. Extract
    df = pd.read_csv('tunisia_houses_raw.csv')
    
    # 2. Transform (Simple cleaning)
    # Example: Ensure no negative prices or impossible areas
    df = df[df['Price'] > 0]
    
    # 3. Load (Connect to SQLite)
    conn = sqlite3.connect('must_university_project.db')
    df.to_sql('houses_warehouse', conn, if_exists='replace', index=False)
    conn.close()
    print("🚀 Data cleaned and loaded into the SQL Warehouse!")

if __name__ == "__main__":
    run_etl()