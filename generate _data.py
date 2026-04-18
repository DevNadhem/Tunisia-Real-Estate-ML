import pandas as pd
import random

cities = ['Tunis', 'Sousse', 'Sfax', 'Bizerte', 'Hammamet']
neighborhoods = {
    'Tunis': ['La Marsa', 'Ennasr', 'Lac 2'],
    'Sousse': ['Kantaoui', 'Sahloul'],
    'Sfax': ['Route de Tunis', 'Ville'],
    'Bizerte': ['Corniche'],
    'Hammamet': ['Yasmine', 'North']
}

def create_fake_data(n=100):
    data = []
    for i in range(n):
        city = random.choice(cities)
        hood = random.choice(neighborhoods[city])
        area = random.randint(50, 350)  # sq meters
        rooms = random.randint(1, 5)
        # Price logic: Base price + (area * multiplier) + noise
        price = 50000 + (area * 1500) + (rooms * 10000) + random.randint(-5000, 5000)
        
        data.append([city, hood, area, rooms, price])
    
    df = pd.DataFrame(data, columns=['City', 'Neighborhood', 'Area', 'Rooms', 'Price'])
    df.to_csv('tunisia_houses_raw.csv', index=False)
    print("✅ Raw data generated successfully!")

if __name__ == "__main__":
    create_fake_data(500)