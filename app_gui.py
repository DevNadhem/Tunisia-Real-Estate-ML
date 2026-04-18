import streamlit as st
import pickle
import pandas as pd

with open('house_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🏠 Tunisia Real Estate Predictor")
st.write("Enter the details below to estimate the market price.")

st.sidebar.header("Property Details")

calc_method = st.sidebar.radio("How do you want to enter the area?", ("Total Area (sqm)", "Dimensions (Length x Width)"))

if calc_method == "Total Area (sqm)":
    area = st.sidebar.number_input("Total Area", min_value=20, max_value=1000, value=120)
else:
    length = st.sidebar.number_input("Length (m)", min_value=1.0, value=10.0)
    width = st.sidebar.number_input("Width (m)", min_value=1.0, value=12.0)
    area = length * width
    st.sidebar.info(f"Calculated Area: {area} sqm")

n_bedrooms = st.sidebar.slider("Number of Bedrooms (n)", 1, 6, 2)
st.sidebar.write(f"Property Type: S+{n_bedrooms}")

if st.button("Predict Price"):
    total_rooms = n_bedrooms + 1
    input_df = pd.DataFrame([[area, total_rooms]], columns=['Area', 'Rooms'])
    prediction = model.predict(input_df)
    
    st.success(f"Estimated Price: {prediction[0]:,.0f} TND")
    st.balloons() # Just for fun!