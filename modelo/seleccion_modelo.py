from modelo.modelo_knn import ChatbotKNN
from modelo.modelo_llm import responder_con_llm

class SelectorDeModelo:
    def __init__(self, usar_knn=True, usar_llm=True):
        self.usar_knn = usar_knn
        self.usar_llm = usar_llm

        if self.usar_knn:
            try:
                self.knn_bot = ChatbotKNN()
            except Exception as e:
                raise RuntimeError(f"Error al inicializar ChatbotKNN: {e}")

    def responder(self, pregunta):
        if not pregunta or not isinstance(pregunta, str):
            return "Pregunta no válida", "Error"

        # Si está activo KNN, se intenta primero con él
        if self.usar_knn:
            respuesta_knn = self.knn_bot.responder(pregunta)
            if respuesta_knn:
                return respuesta_knn, "KNN"

        # Si está activo LLM y no hubo respuesta de KNN o está desactivado
        if self.usar_llm:
            respuesta_llm = responder_con_llm(pregunta)
            if respuesta_llm:
                return respuesta_llm, "LLM"

        return "No se pudo generar una respuesta", "Error"
