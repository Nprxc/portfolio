# Assistant Cadeaux IA

Ce projet fournit un petit assistant web pour recommander des idées de cadeaux personnalisés. Il s'appuie sur **FastAPI** pour le backend et un simple formulaire HTML pour l'interface.

## Installation

1. Clonez le dépôt puis installez les dépendances :
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Lancez le serveur local :
   ```bash
   ./run.sh
   ```
3. Ouvrez <http://localhost:8000> dans votre navigateur pour discuter avec l'IA.

## Tests

Des tests de base sont disponibles avec **pytest** :
```bash
pytest
```

## Docker

Une image Docker peut être construite et exécutée :
```bash
docker build -t assistant-cadeaux .
docker run -p 8000:8000 assistant-cadeaux
```

## Arborescence principale

- `app/` – Backend FastAPI
- `templates/` – Modèle HTML
- `data/catalog.json` – Catalogue produit (vide pour le moment)
- `ia_engine.py` – Fonction de génération de réponse (placeholder)
- `tests/` – Tests unitaires
