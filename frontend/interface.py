#front

import streamlit as st
import requests
from backend.app.main import url
#interface simple, basique, ordinaire, quelconque, sombre, banale et directe
st.title('preuve maxime manon', text_alignment="center", color='pink')

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