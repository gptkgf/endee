import numpy as np

class Endee:
    def __init__(self):
        self.vectors = []
        self.texts = []

    def add(self, embeddings, docs):
        for emb, doc in zip(embeddings, docs):
            self.vectors.append(emb)
            self.texts.append(doc)

    def search(self, query_embedding, top_k=2):
        scores = []
        for v in self.vectors:
            score = np.dot(v, query_embedding[0]) / (
                np.linalg.norm(v) * np.linalg.norm(query_embedding[0])
            )
            scores.append(score)

        top_indices = np.argsort(scores)[-top_k:][::-1]
        return [self.texts[i] for i in top_indices]
