import os
import pickle
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# --- CONFIGURACIÓN GLOBAL ---
MODELO_EMBEDDINGS = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# --- FUNCIÓN PARA GENERAR EMBEDDINGS DESDE UN SOLO PDF ---
def generar_embeddings_pdf(ruta_pdf, nombre_salida):
    """
    Entrena un modelo de vectorización a partir del contenido de un único archivo PDF.
    """
    if not os.path.exists(ruta_pdf):
        raise FileNotFoundError(f"El archivo '{ruta_pdf}' no existe.")

    with pdfplumber.open(ruta_pdf) as pdf:
        texto = ""
        for pagina in pdf.pages:
            texto += pagina.extract_text() or ""

    if not texto.strip():
        raise ValueError("No se pudo extraer texto del PDF.")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = text_splitter.split_text(texto)

    embeddings = HuggingFaceEmbeddings(model_name=MODELO_EMBEDDINGS)
    vectorstore = FAISS.from_texts(chunks, embedding=embeddings)

    with open(nombre_salida, "wb") as f:
        pickle.dump(vectorstore, f)
        
    print(f"Modelo guardado en '{nombre_salida}' con {len(chunks)} fragmentos de texto.")