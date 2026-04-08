#front

import streamlit as st
import requests
import os

url = os.getenv('BACKEND_URL', 'http://localhost:8000')

st.title('interface simple, basique, ordinaire, quelconque, sombre, banale et directe', text_alignment="center")

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

    st.write('espèce prédite:', data['prediction'], text_align="center")