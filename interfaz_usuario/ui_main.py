import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import interfaz_usuario.ui_inicio_sesion as ui_inicio_sesion
import interfaz_usuario.ui_informacion as ui_informacion
import interfaz_usuario.ui_chat_bot as ui_chat_bot
from modelo.seleccion_modelo import SelectorDeModelo
# ────────────────────────────────────────────────────────────────────────────
# 1) Configuración GLOBAL de la página: DEBE ser la primera llamada a st.*
# ────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Goit-IA",
    page_icon="🤖",
    layout="wide"
)

# ────────────────────────────────────────────────────────────────────────────
# 2) Estado de navegación en la sesión
# ────────────────────────────────────────────────────────────────────────────

# Inicializar estado de navegación
if "page" not in st.session_state:
    st.session_state.page = "main"

# Luego ya puedes hacer esto sin error:
if st.session_state.page == "main":
    # contenido de inicio
    pass
elif st.session_state.page == "chat":
    # contenido del chat
    pass

with st.container():
    col_logo, col_nav = st.columns([2, 1])

    with col_logo:
        st.image("logo.png", use_container_width=False, width=200)

    with col_nav:
        # Espacio a la izquierda + 3 columnas iguales para los botones
        spacer, btn1, btn2, btn3 = st.columns([1, .8, .9, 1.1])
        with btn1:
            if st.button("Inicio"):
                st.session_state.page = "main"
        with btn2:
            if st.button("Chat-Bot"):
                st.session_state.page = "chat"
        with btn3:
            if st.button("Iniciar sesión"):
                st.session_state.page = "login"


# Cambiar de página según el enlace seleccionado
if "go" in st.query_params:
    st.session_state.page = st.query_params["go"]


# ────────────────────────────────────────────────────────────────────────────
# 4) LÓGICA DE PÁGINAS
# ────────────────────────────────────────────────────────────────────────────
if st.session_state.page == "main":
    # Títulos centrales
    st.markdown("<h1 style='text-align: center;'>Goit-IA</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Asistente Virtual</h3>", unsafe_allow_html=True)
    st.write("")  # Espacio en blanco extra opcional

    if st.button("Ir al Chat-Bot"):
        st.session_state.page = "chat"




elif st.session_state.page == "login":
    ui_inicio_sesion.app()

elif st.session_state.page == "info":
    ui_informacion.app()

elif st.session_state.page == "chat":
    # ✅ Inicializa selector_modelo si no existe
    if "selector_modelo" not in st.session_state:
        st.session_state.selector_modelo = SelectorDeModelo()
    ui_chat_bot.app()
