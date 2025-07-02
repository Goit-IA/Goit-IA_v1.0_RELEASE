import pickle
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate

# Ruta completa al archivo .pkl
RUTA_VECTORSTORE = "../modelo/vector_info_general.pkl"

def responder_con_llm(pregunta):
    try:
        # Cargar vectorstore
        with open(RUTA_VECTORSTORE, "rb") as f:
            vectorstore: FAISS = pickle.load(f)

        documentos = vectorstore.similarity_search(query=pregunta, k=3)

        if not documentos:
            return "No encontré una respuesta a tu pregunta."

        # Modelo LLM actualizado
        llm = OllamaLLM(
            model="mistral:7b",
            temperature=0.3,
            top_p=0.8,
            top_k=40,
            num_ctx=2048,
            num_predict=256,
            repeat_penalty=1.3
        )

        # Plantilla de prompt
        prompt = PromptTemplate.from_template(
            "Pregunta del usuario: {pregunta}\n\n"
            "Responde únicamente con la información proporcionada en el contexto a continuación. "
            "No inventes información. Si no puedes encontrar una respuesta clara en el contexto, responde 'No encontré una respuesta adecuada.'\n\n"
            "Contexto:\n{context}"
        )

        # Nueva cadena basada en documentos tipo "stuff"
        chain = create_stuff_documents_chain(llm=llm, prompt=prompt)

        # Ejecutar con invoke en vez de .run()
        respuesta = chain.invoke({
            "context": documentos,
            "pregunta": pregunta
        })

        texto = respuesta.strip()
        if not texto or texto.lower().startswith("i don't know") or "lo siento" in texto.lower():
            return "No encontré una respuesta adecuada."
        return texto

    except Exception as e:
        return f"⚠️ Error al generar respuesta con LLM: {e}"
