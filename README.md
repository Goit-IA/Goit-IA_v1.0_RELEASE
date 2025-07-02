# Goit-IA: Asistente Virtual Inteligente

**Goit-IA** es un asistente virtual desarrollado con Python y Streamlit, capaz de responder preguntas frecuentes de usuarios, entrenarse con archivos PDF y utilizar tanto un modelo KNN como un modelo LLM (Ollama/Mistral) para ofrecer respuestas precisas y contextualizadas.

---

## Características principales

- **Interfaz web interactiva** con Streamlit.
- **Chat-Bot** con historial de mensajes y saludo animado.
- **Inicio de sesión** para control de acceso.
- **Carga y entrenamiento de PDFs**: une archivos y genera embeddings automáticos.
- **Modelo híbrido**:
  - **KNN**: búsqueda rápida en una base de datos de preguntas frecuentes.
  - **LLM**: generación de respuestas complejas a partir de información en PDFs, usando modelos locales (Ollama/Mistral).
- **Gestión de usuarios** mediante CSV.
- **Estructura modular y escalable**.

---

## Estructura del proyecto

```
.
├── interfaz_usuario/
│   ├── ui_main.py              # Página principal y navegación
│   ├── ui_chat_bot.py          # Interfaz del chat
│   ├── ui_informacion.py       # Carga/entrenamiento de PDFs
│   └── ui_inicio_sesion.py     # Inicio de sesión
├── modelo/
│   ├── entrenamiento.py        # Generación de embeddings desde PDFs
│   ├── modelo_knn.py           # Modelo de preguntas frecuentes KNN
│   ├── modelo_llm.py           # Modelo LLM (Ollama/Mistral)
│   └── seleccion_modelo.py     # Selector automático de modelo
│   └── vector_info_general.pkl # Embeddings generados de los PDFs  
├── datasets/
│   └── users.csv               # Usuarios registrados
│   └── faq.csv                 # Preguntas y respuestas frecuentes
├── pdfs/
│   └── documento_unido.pdf     # PDF combinado para entrenamiento
├── logo.png                    # Logo del proyecto
```

---

## Instalación

1. **Clona el repositorio**

   ```bash
   git clone https://github.com/Goit-IA/Goit-IA_v1.0_RELEASE.git
   cd Goit-IA_v1.0_RELEASE
   ```

2. **Crea un entorno virtual y activa:**

   ```bash
   python -m venv my_env
   source my_env/bin/activate  # En Windows: my_env\Scripts\activate
   ```

3. **Instala dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

   Dependencias principales:

   - streamlit
   - pandas
   - scikit-learn
   - PyPDF2
   - pdfplumber
   - langchain
   - langchain\_community
   - langchain\_ollama
   - sentence-transformers

4. **Ejecuta la aplicación:**

   ```bash
   streamlit run interfaz_usuario/ui_main.py
   ```

---

## Uso del sistema

1. **Inicio**: Navega entre Inicio, Chat-Bot e Inicio de sesión mediante la barra superior.
2. **Inicio de sesión**: Accede con usuario y contraseña. (Usuarios en `/datasets/users.csv`)
3. **Carga de PDFs**: Sube uno o varios PDFs. El sistema los une y genera embeddings para respuestas contextuales.
4. **Chat-Bot**: Haz preguntas. El bot primero intentará responder usando KNN (FAQ) y, si no encuentra respuesta, usará el modelo LLM (entrenado con tus PDFs).
5. **Entrenamiento**: Cada vez que se suben nuevos PDFs, el sistema se reentrena automáticamente.

---

## Modelos utilizados

- **KNN**: Busca respuestas rápidas en el archivo `faq.csv` usando similitud euclidiana sobre TF-IDF.
- **LLM (Ollama/Mistral)**: Si no encuentra respuesta en el FAQ, utiliza un modelo de lenguaje grande entrenado localmente para generar una respuesta con información de los PDFs cargados.

---

## Personalización

- **Agregar FAQs**: Edita `datasets/faq.csv`.
- **Usuarios**: Edita `datasets/users.csv`.
- **Entrenamiento**: Sube PDFs desde la interfaz y se actualizarán los embeddings automáticamente.

---

## Créditos y contacto

Desarrollado por el equipo de Goit-IA.

¿Dudas o mejoras? ¡Contribuciones y sugerencias son bienvenidas!

---

