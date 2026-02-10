from sentence_transformers import SentenceTransformer
from endee import Endee

model = SentenceTransformer("all-MiniLM-L6-v2")
db = Endee()

query = input("Enter your query: ")

query_embedding = model.encode([query])
results = db.search(query_embedding, top_k=2)

print("\nTop Results:")
for r in results:
    print(r)
