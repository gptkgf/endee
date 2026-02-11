import os
from sentence_transformers import SentenceTransformer
from endee import Endee

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create vector DB
db = Endee()

# Load documents
base_dir = os.path.dirname(os.path.abspath(__file__))
docs_path = os.path.join(base_dir, "data", "docs.txt")

with open(docs_path, "r", encoding="utf-8") as f:
    docs = [line.strip() for line in f if line.strip()]

# Store embeddings
embeddings = model.encode(docs)
db.add(embeddings, docs)

def rag_answer(question):
    q_emb = model.encode([question])
    results = db.search(q_emb, top_k=1)

    if not results:
        return (
            "Sorry \n"
            "I couldn’t find an answer related to this question."
        )

    return (
        "Sure! \n\n"
        f"{results[0]}\n\n"
        "Ask me another question if you like!"
    )
