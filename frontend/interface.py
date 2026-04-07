#front

import streamlit as st

st.title('interface simple, basique, ordinaire, quelconque, sombre, banale et directe')
col1, col2 = st.columns(2)
with col1:
    st.subheader('données sur les pétales')
    st.number_input('longueur de la pétale')
    st.number_input('largeur de la pétale')

with col2:
    st.subheader('données sur les sépales')
    st.number_input('longueur de la sépale')
    st.number_input('largeur de la sépale')

if st.button('envoyer'):
    pass