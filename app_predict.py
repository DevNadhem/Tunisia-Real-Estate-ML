import pickle
import pandas as pd

with open('house_model.pkl', 'rb') as f:
    model = pickle.load(f)

print("--- 🏠 Tunisia House Price Predictor (S+n) ---")

choice = input("Do you know the total area in sqm? (yes/no): ").lower()

if choice == 'yes':
    area = float(input("Enter total area: "))
else:
    length = float(input("Enter length (m): "))
    width = float(input("Enter width (m): "))
    area = length * width
    print(f"👉 Calculated Area: {area} sqm")

n_bedrooms = int(input("Enter number of bedrooms (the 'n' in S+n): "))
total_rooms = n_bedrooms + 1 # Converting S+n to total rooms for the model

new_data = pd.DataFrame([[area, total_rooms]], columns=['Area', 'Rooms'])
prediction = model.predict(new_data)

print("-" * 40)
print(f"🏠 Type: S+{n_bedrooms}")
print(f"💰 Estimated Market Price: {prediction[0]:,.0f} TND")
print("-" * 40)