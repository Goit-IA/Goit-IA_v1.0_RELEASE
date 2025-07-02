import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


class ChatbotKNN:
    def __init__(self, ruta_csv="../datasets/faq.csv"):
        self.df = pd.read_csv(ruta_csv, encoding='utf-8')
        self.vectorizador = TfidfVectorizer()
        self.X = self.vectorizador.fit_transform(self.df['Pregunta'])
        self.modelo = NearestNeighbors(n_neighbors=3, metric='euclidean')
        self.modelo.fit(self.X)

    def responder(self, pregunta_usuario, umbral=0.4):
        pregunta_vector = self.vectorizador.transform([pregunta_usuario])
        distancia, indice = self.modelo.kneighbors(pregunta_vector)
        if distancia[0][0] > umbral:
            return None  # No se encontró una coincidencia suficientemente cercana
        return self.df.iloc[indice[0][0]]['Respuesta']
