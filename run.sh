#!/bin/bash
# Launch the FastAPI server using uvicorn
# uvicorn app.main:app --host 0.0.0.0 --port 8000


#!/bin/bash

# Couleurs terminal
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Démarrage de l'application FastAPI - Assistant Cadeau 🎁${NC}"

# Vérifie que le dossier venv existe
if [ ! -d "venv" ]; then
    echo -e "${RED}❌ Environnement virtuel 'venv/' introuvable.${NC}"
    echo -e "${YELLOW}➡️  Veuillez le créer avec : python3 -m venv venv${NC}"
    exit 1
fi

# Active l'environnement virtuel
echo -e "${GREEN}📦 Activation de l'environnement virtuel...${NC}"
source venv/bin/activate

# Lancer le serveur
echo -e "${GREEN}🌐 Lancement du serveur FastAPI avec Uvicorn${NC}"
echo -e "${YELLOW}👉 Accessible sur : http://localhost:8000${NC}"

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Affichage après arrêt
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Serveur arrêté proprement.${NC}"
else
    echo -e "${RED}⚠️ Une erreur est survenue lors du lancement de l'API.${NC}"
fi