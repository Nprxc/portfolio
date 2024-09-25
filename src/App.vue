<template>
  <div id="app" class="app-container">
    <!-- Message de bienvenue -->
    <div class="welcome-message">
      <h1>Bienvenue sur mon portfolio</h1>
      <p>
        Explorez mes compétences, mes expériences, et découvrez qui je suis en cliquant sur les différentes sections ci-dessous.
      </p>
    </div>

    <!-- Grille des sections principales avec une intégration plus douce au background -->
    <div class="grid-container">
      <!-- Section 1: Qui suis-je -->
      <div class="grid-item" @click="openModal('quiSuisJe')">
        <h3>Qui suis-je ?</h3>
      </div>

      <!-- Section 2: Parcours Académique -->
      <div class="grid-item" @click="openModal('parcoursAcademique')">
        <h3>Parcours Académique</h3>
      </div>

      <!-- Section 3: Expériences Pro -->
      <div class="grid-item" @click="openModal('experiencesPro')">
        <h3>Expériences Pro</h3>
      </div>

      <!-- Section 4: Compétences -->
      <div class="grid-item" @click="openModal('competences')">
        <h3>Compétences</h3>
      </div>

      <!-- Section 5: Liens Utiles -->
      <div class="grid-item" @click="openModal('liensUtiles')">
        <h3>Liens Utiles</h3>
      </div>
    </div>

    <!-- Modales pour afficher les composants correspondants -->
    <div v-if="activeModal === 'quiSuisJe'" class="modal">
      <div class="modal-content">
        <QuiSuisJe />
        <button @click="closeModal">Fermer</button>
      </div>
    </div>

    <div v-if="activeModal === 'parcoursAcademique'" class="modal">
      <div class="modal-content">
        <ParcoursAcademique />
        <button @click="closeModal">Fermer</button>
      </div>
    </div>

    <div v-if="activeModal === 'experiencesPro'" class="modal">
      <div class="modal-content">
        <ExperiencesPro />
        <button @click="closeModal">Fermer</button>
      </div>
    </div>

    <div v-if="activeModal === 'competences'" class="modal">
      <div class="modal-content">
        <Competences />
        <button @click="closeModal">Fermer</button>
      </div>
    </div>

    <div v-if="activeModal === 'liensUtiles'" class="modal">
      <div class="modal-content">
        <LiensUtiles />
        <button @click="closeModal">Fermer</button>
      </div>
    </div>
  </div>
</template>

<script>
import QuiSuisJe from './components/QuiSuisJe.vue';
import ParcoursAcademique from './components/ParcoursAcademique.vue';
import ExperiencesPro from './components/ExperiencesPro.vue';
import Competences from './components/Competences.vue';
import LiensUtiles from "@/components/LiensUtiles.vue";

export default {
  data() {
    return {
      activeModal: null, // Pour suivre la modale active
    };
  },
  components: {
    QuiSuisJe,
    ParcoursAcademique,
    ExperiencesPro,
    Competences,
    LiensUtiles,
  },
  methods: {
    openModal(modalName) {
      this.activeModal = modalName;
    },
    closeModal() {
      this.activeModal = null;
    },
  },
};
</script>

<style scoped>
/* Ajustement du fond pour l'intégration */
html, body {
  background-color: #1a1a1a;
  color: white;
  height: 100%;
  margin: 0;
  padding: 0;
  font-family: 'Arial', sans-serif;
}

/* Message de bienvenue */
.welcome-message {
  text-align: center;
  margin-bottom: 2rem;
  animation: fadeIn 1.5s ease-in-out;
}

.welcome-message h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.welcome-message p {
  font-size: 1.2rem;
  color: #cccccc;
}

/* Grille principale avec des cartes plus intégrées */
.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* S'adapte à la largeur disponible */
  gap: 1.5rem;
  padding: 2rem;
  margin: 0 auto;
  max-width: 1200px;
}

/* Style des cartes */
.grid-item {
  background-color: #2c2c2c;
  color: white;
  padding: 2rem;
  border-radius: 12px;
  text-align: center;
  transition: box-shadow 0.3s ease, transform 0.3s ease;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}

.grid-item h3 {
  margin: 0;
  font-size: 1.5rem;
}

/* Effet subtil au survol */
.grid-item:hover {
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.5);
  transform: translateY(-5px);
}

/* Styles des modales */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: #ffffff;
  padding: 2rem;
  max-width: 800px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
  border-radius: 12px;
  text-align: left;
  position: relative;
}

/* Bouton fermer */
button {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 0.5rem 1rem;
  background-color: #333;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #555;
}

/* Animation d'apparition */
.modal-content {
  animation: fadeInUp 0.5s ease;
}

@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translateY(30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Animation du message de bienvenue */
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(-30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
