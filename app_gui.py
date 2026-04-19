import streamlit as st
import pickle
import pandas as pd

# 1. Define the Translation Dictionary
languages = {
    "English": {
        "title": "🏠 Tunisia Real Estate Predictor",
        "header": "Enter the details below to estimate the market price.",
        "sidebar_header": "Property Details",
        "method_label": "How do you want to enter the area?",
        "method_options": ("Total Area (sqm)", "Dimensions (Length x Width)"),
        "area_label": "Total Area",
        "length_label": "Length (m)",
        "width_label": "Width (m)",
        "calc_area_msg": "Calculated Area:",
        "rooms_label": "Number of Bedrooms (n)",
        "type_label": "Property Type:",
        "predict_btn": "Predict Price",
        "result": "Estimated Price:"
    },
    "Français": {
        "title": "🏠 Estimateur Immobilier Tunisie",
        "header": "Entrez les détails ci-dessous pour estimer le prix du marché.",
        "sidebar_header": "Détails de la propriété",
        "method_label": "Comment voulez-vous saisir la surface ?",
        "method_options": ("Surface totale (m²)", "Dimensions (Longueur x Largeur)"),
        "area_label": "Surface totale",
        "length_label": "Longueur (m)",
        "width_label": "Largeur (m)",
        "calc_area_msg": "Surface calculée :",
        "rooms_label": "Nombre de chambres (n)",
        "type_label": "Type de propriété :",
        "predict_btn": "Prédire le prix",
        "result": "Prix estimé :"
    },
    "العربية": {
        "title": "🏠 مستشار العقارات في تونس",
        "header": "أدخل التفاصيل أدناه لتقدير سعر السوق.",
        "sidebar_header": "تفاصيل العقار",
        "method_label": "كيف تريد إدخال المساحة؟",
        "method_options": ("المساحة الإجمالية (م²)", "الأبعاد (الطول × العرض)"),
        "area_label": "المساحة الإجمالية",
        "length_label": "الطول (م)",
        "width_label": "العرض (م)",
        "calc_area_msg": "المساحة المحتسبة:",
        "rooms_label": "عدد غرف النوم (n)",
        "type_label": "نوع العقار:",
        "predict_btn": "توقع السعر",
        "result": "السعر التقديري:"
    }
}

# 2. Sidebar Language Selector
selected_lang = st.selectbox("Choose your language / Choisissez votre langue / اختر لغتك", ["English", "Français", "العربية"])
lang = languages[selected_lang]

st.divider()

# 3. Load the Model
with open('house_model.pkl', 'rb') as f:
    model = pickle.load(f)

# 4. Use the 'lang' variable for all UI text
st.title(lang["title"])
st.write(lang["header"])

st.sidebar.header(lang["sidebar_header"])

calc_method = st.sidebar.radio(lang["method_label"], lang["method_options"])

if calc_method == lang["method_options"][0]: # Total Area
    area = st.sidebar.number_input(lang["area_label"], min_value=20, max_value=1000, value=120)
else:
    length = st.sidebar.number_input(lang["length_label"], min_value=1.0, value=10.0)
    width = st.sidebar.number_input(lang["width_label"], min_value=1.0, value=12.0)
    area = length * width
    st.sidebar.info(f"{lang['calc_area_msg']} {area} sqm")

n_bedrooms = st.sidebar.slider(lang["rooms_label"], 1, 6, 2)
st.sidebar.write(f"{lang['type_label']} S+{n_bedrooms}")

if st.button(lang["predict_btn"]):
    total_rooms = n_bedrooms + 1
    input_df = pd.DataFrame([[area, total_rooms]], columns=['Area', 'Rooms'])
    prediction = model.predict(input_df)
    
    st.success(f"{lang['result']} {prediction[0]:,.0f} TND")
    st.balloons()