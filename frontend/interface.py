#front

import streamlit as st
import requests
import os

url = os.getenv('BACKEND_URL', 'http://localhost:8000')
st.markdown(
    "<h1 style='text-align: center; color: pink;'>"
    "interface simple, basique, ordinaire, quelconque, sombre, banale et directe"
    "</h1>",
    unsafe_allow_html=True
)
col1, col2 = st.columns(2)

with col1:
    st.subheader('données sur les pétales')
    lo_pe = st.number_input('longueur de la pétale')
    la_pe = st.number_input('largeur de la pétale')

with col2:
    st.subheader('données sur les sépales')
    lo_se = st.number_input('longueur de la sépale')
    la_se = st.number_input('largeur de la sépale')

if st.button('envoyer'):
    response = requests.post(f"{url}/predict",
                           json={'longueur_petale' : lo_pe,
                                'largeur_petale' : la_pe,
                                'longueur_sepale' : lo_se,
                                'largeur_sepale' : la_se })
    data = response.json()

    st.markdown(
        f"<p style='text-align: center;'>espèce prédite : {data['prediction']}</p>",
        unsafe_allow_html=True
    )