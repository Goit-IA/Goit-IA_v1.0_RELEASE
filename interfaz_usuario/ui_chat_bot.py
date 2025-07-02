import streamlit as st
import time
from modelo.seleccion_modelo import SelectorDeModelo

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Instanciar el selector una sola vez
if "selector_modelo" not in st.session_state:
    st.session_state.selector_modelo = SelectorDeModelo()

def app():
    st.markdown("<h2 style='text-align: center;'>Chat-Bot</h2>", unsafe_allow_html=True)
    st.markdown("---")

    # Inicializar historial
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar saludo animado si es primera vez
    if "saludo_mostrado" not in st.session_state:
        saludo = "Hola 👋, soy Goit-IA. ¿En qué puedo ayudarte hoy?"
        with st.chat_message("assistant"):
            placeholder = st.empty()
            texto = ""
            for letra in saludo:
                texto += letra
                placeholder.markdown(texto)
                time.sleep(0.04)
        st.session_state.messages.append({"sender": "assistant", "text": saludo})
        st.session_state.saludo_mostrado = True

    # Mostrar mensajes previos
    for msg in st.session_state.messages:
        if st.session_state.messages.index(msg) == 0 and "saludo_mostrado" in st.session_state:
            continue
        with st.chat_message(msg["sender"]):
            st.markdown(msg["text"])

    # Entrada del usuario
    user_input = st.chat_input("Escribe un mensaje…")
    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)
        st.session_state.messages.append({"sender": "user", "text": user_input})

        with st.chat_message("assistant"):
            with st.spinner("Generando respuesta..."):
                time.sleep(3)
                respuesta, modelo = st.session_state.selector_modelo.responder(user_input)  # ✅ CAMBIO
                st.markdown(respuesta + f"\n\n_(Modelo: {modelo})_")  # opcional: mostrar modelo usado

        st.session_state.messages.append({"sender": "assistant", "text": respuesta})
