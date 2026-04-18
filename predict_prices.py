import pandas as pd
import sqlite3
from sklearn.linear_model import LinearRegression
import jobpy # To save the model

def train_model():
    # Pull data from SQL
    conn = sqlite3.connect('must_university_project.db')
    df = pd.read_sql('SELECT * FROM houses_warehouse', conn)
    conn.close()

    # Prep data (ML models need numbers)
    # We will use 'Area' and 'Rooms' to predict 'Price'
    X = df[['Area', 'Rooms']]
    y = df['Price']

    # Train
    model = LinearRegression()
    model.fit(X, y)
    
    print(f"📈 Model Trained! Accuracy (R2): {model.score(X, y):.2f}")
    
    # Save the 'Machine' for later use
    import pickle
    with open('house_model.pkl', 'wb') as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_model()