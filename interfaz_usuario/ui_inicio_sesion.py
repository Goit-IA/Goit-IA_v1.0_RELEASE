import streamlit as st
import pandas as pd
import os

def app():
    st.title("Inicio de sesión")

    if not os.path.exists("../datasets/users.csv"):
        df_users = pd.DataFrame({"username", "password"})
        df_users.to_csv("../datasets/users.csv", index=False)

    df = pd.read_csv("../datasets/users.csv")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Login"):
        matched_user = df[(df.username == username) & (df.password == password)]
        if not matched_user.empty:
            st.success("Autenticación exitosa")
            st.session_state.usuario = username  # Guardamos quién inició sesión
            st.session_state.page = "info"       # Redirigimos a la interfaz de información
        else:
            st.error("Usuario o contraseña incorrectos")

    if st.button("Volver al inicio"):
        st.session_state.page = "main"
