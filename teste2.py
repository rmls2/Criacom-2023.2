
""" lista = []
with open('./inputusuario.txt', 'r') as f:
    for linha in f: 
        lista.append(linha.strip())

print(lista) """

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Paragrafo 1")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("Paragrafo 2")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("Paragrafo 3")
   st.image("https://static.streamlit.io/examples/owl.jpg")