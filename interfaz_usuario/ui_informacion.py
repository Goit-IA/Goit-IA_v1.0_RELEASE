import streamlit as st
import os
import sys
import shutil
from PyPDF2 import PdfMerger
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelo.entrenamiento import generar_embeddings_pdf

def app():
    if "usuario" not in st.session_state:
        st.warning("Debe iniciar sesión para acceder a esta sección.")
        return

    st.title("Carga y Entrenamiento con PDFs")

    # Crear carpeta si no existe
    carpeta_destino = "../pdfs"
    os.makedirs(carpeta_destino, exist_ok=True)

    archivos_pdf = st.file_uploader("Sube uno o varios archivos PDF", type=["pdf"], accept_multiple_files=True)

    if archivos_pdf:
        st.markdown("### Archivos recibidos:")
        for archivo in archivos_pdf:
            ruta_destino = os.path.join(carpeta_destino, archivo.name)
            with open(ruta_destino, "wb") as f:
                f.write(archivo.read())
            st.write(f"📄 {archivo.name}")

        # Unir PDFs
        ruta_pdf_unido = os.path.join(carpeta_destino, "documento_unido.pdf")
        merger = PdfMerger()
        for archivo in archivos_pdf:
            merger.append(os.path.join(carpeta_destino, archivo.name))
        merger.write(ruta_pdf_unido)
        merger.close()
        st.success("✅ Archivos PDF unidos exitosamente")

        # Entrenar modelo con el PDF unido
        try:
            generar_embeddings_pdf(ruta_pdf_unido, "../modelo/vector_info_general.pkl")
            st.success("✅ Modelo entrenado con el PDF unido")
        except Exception as e:
            st.error(f"❌ Error durante el entrenamiento: {e}")

    st.markdown("---")

    if st.button("Volver al inicio"):
        st.session_state.page = "main"
