<template>
  <div class="parcours-container">
    <h1 class="title">Parcours Académique</h1>

    <div class="section">
      <h2 @click="toggleSection('mpsi')" class="clickable">
        <span v-if="!sections.mpsi">▶️</span>
        <span v-if="sections.mpsi">🔽</span>
        <span class="section-title">Classe Préparatoire MPSI - Mariette</span>
      </h2>
      <transition name="slide-fade">
        <ul v-if="sections.mpsi" class="details-list">
          <li><i class="fas fa-calculator"></i> Mathématiques</li>
          <li><i class="fas fa-atom"></i> Physique</li>
          <li><i class="fas fa-laptop-code"></i> Informatique</li>
          <li><i class="fas fa-brain"></i> Logique</li>
        </ul>
      </transition>
    </div>

    <div class="section">
      <h2 @click="toggleSection('isen')" class="clickable">
        <span v-if="!sections.isen">▶️</span>
        <span v-if="sections.isen">🔽</span>
        <span class="section-title">Grande École d'Ingénieur - ISEN Cybersécurité</span>
      </h2>
      <transition name="slide-fade">
        <ul v-if="sections.isen" class="details-list">
          <li><i class="fas fa-code"></i> Développement Web (Front-end & Back-end)</li>
          <li><i class="fas fa-network-wired"></i> Network & Systems</li>
          <li><i class="fas fa-shield-alt"></i> Pentesting</li>
          <li><i class="fas fa-bug"></i> Analyse des vulnérabilités logicielles</li>
          <li><i class="fas fa-robot"></i> Intelligence Artificielle</li>
        </ul>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sections: {
        mpsi: false,
        isen: false,
      },
    };
  },
  methods: {
    toggleSection(section) {
      this.sections[section] = !this.sections[section];
    },
  },
};
</script>

<style scoped>
/* Conteneur principal */
.parcours-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  min-height: 100vh;
  padding-left: 2rem;
  background-color: white;
  color: black;
}

.title {
  font-size: 2.5rem;
  margin-bottom: 3rem;
  text-align: left;
  width: 100%;
  color: black;
}

/* Section */
.section {
  margin-bottom: 2rem;
}

.clickable {
  cursor: pointer;
  font-size: 1.6rem;
  display: flex;
  align-items: center;
  transition: transform 0.2s, color 0.2s;
}

.section-title {
  margin-left: 0.5rem;
}

/* Effet de survol */
.clickable:hover {
  transform: scale(1.02);
  color: #007bff;
}

/* Détails de la liste */
.details-list {
  list-style-type: none;
  padding-left: 1.5rem;
  margin-top: 1rem;
}

.details-list li {
  margin: 0.5rem 0;
  font-size: 1.4rem;
  color: black;
}

.details-list li i {
  margin-right: 0.5rem;
  color: #007bff; /* Couleur des icônes */
}

/* Animation pour l'affichage des sections */
.slide-fade-enter-active {
  transition: all 0.5s ease;
}
.slide-fade-leave-active {
  transition: all 0.5s ease;
}
.slide-fade-enter, .slide-fade-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}
</style>
