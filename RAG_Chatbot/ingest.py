from sentence_transformers import SentenceTransformer
from endee import Endee

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load documents
with open("data/docs.txt", "r") as f:
    docs = [line.strip() for line in f if line.strip()]

# Create embeddings
embeddings = model.encode(docs)

# Store in Endee
db = Endee()
db.add(embeddings, docs)

print("Documents successfully stored in Endee Vector DB")
