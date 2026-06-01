from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "Delhi receives heavy rainfall"

embedding = model.encode(text)

print(len(embedding))
print(embedding[:10])