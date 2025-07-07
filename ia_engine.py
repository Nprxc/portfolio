import json
import faiss
import os
import httpx
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Charger le catalogue
with open("data/catalog.json", "r") as f:
    catalog = json.load(f)

# Appel API Mistral
def mistral_api_generate(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistral-tiny",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 512
    }

    response = httpx.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=15
    )
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

# Classe Agent IA pour gérer une session de chat
class GiftAssistantAgent:
    def __init__(self):
        self.catalog = catalog
        self.product_texts = [f"{p['titre']} - {p['description']}" for p in self.catalog]
        self.model_embed = SentenceTransformer("all-MiniLM-L6-v2")
        self.product_vectors = self.model_embed.encode(self.product_texts)
        self.index = faiss.IndexFlatL2(self.product_vectors[0].shape[0])
        self.index.add(self.product_vectors)
        self.history = []
        self.current_choice = None  # Produit choisi par le client

    def retrieve_similar_products(self, question, k=3):
        q_vec = self.model_embed.encode([question])
        distances, indices = self.index.search(q_vec, k)
        return [self.catalog[i] for i in indices[0]]

    def generate(self, question: str) -> str:
        # Mise à jour du choix actuel si mention explicite
        if any(keyword in question.lower() for keyword in ["je veux", "je prends", "je choisis", "j'aimerais", "je souhaite", "je vais prendre", "je vais offrir"]):
            produits = self.retrieve_similar_products(question, k=1)
            if produits:
                self.current_choice = produits[0]

        # Récupérer produits similaires uniquement si pas de choix actuel
        if self.current_choice:
            produits = [self.current_choice]
        else:
            produits = self.retrieve_similar_products(question)

        contexte = "\n".join([f"- {p['titre']} : {p['description']}" for p in produits])
        historique = "\n".join([f"{m['role']}: {m['text']}" for m in self.history])

        prompt = f"""
Tu es un assistant IA commercial expert en cadeaux personnalisés.

Voici les produits à considérer :
{contexte}

Conversation précédente avec le client :
{historique}

Nouvelle question du client :
{question}

Consignes importantes :
- Si un produit a été choisi précédemment, n’en propose plus d'autres sauf demande explicite.
- Rappelle subtilement que le cadeau est personnalisable, livré rapidement et très apprécié.
- Si le client demande un prix, donne celui du produit choisi s’il est connu.
- Aide à conforter la décision du client s’il a déjà fait un choix.
- Reste chaleureux, pertinent, synthétique et sans phrases inutiles.
- Ne redis pas l’ensemble du catalogue.
- Utilise un langage simple, clair et bienveillant, comme un conseiller client professionnel.

Réponds maintenant :
"""

        self.history.append({"role": "user", "text": question})
        response = mistral_api_generate(prompt)
        self.history.append({"role": "assistant", "text": response})
        return response