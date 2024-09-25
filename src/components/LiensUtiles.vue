<template>
  <div class="liens-utiles-container">
    <div class="grid">
      <!-- Téléphone -->
      <div class="icon-container">
        <a href="tel:+33605082747" class="icon-link">
          <img src="/src/assets/img/phone-icon.png" alt="Téléphone" class="icon" />
          <p class="icon-description">Téléphone</p>
        </a>
      </div>

      <!-- RootMe -->
      <div class="icon-container">
        <a href="https://www.root-me.org/Nprxc?lang=fr#ec284a994776c4a3f92927e2d3a53185" target="_blank" class="icon-link">
          <img src="/src/assets/img/rootme-icon.png" alt="RootMe" class="icon" />
          <p class="icon-description">RootMe</p>
        </a>
      </div>

      <!-- LinkedIn -->
      <div class="icon-container">
        <a href="https://www.linkedin.com" target="_blank" class="icon-link">
          <img src="/src/assets/img/linkedin-icon.png" alt="LinkedIn" class="icon" />
          <p class="icon-description">LinkedIn</p>
        </a>
      </div>

      <!-- Mail -->
      <div class="icon-container">
        <a href="mailto:guy.axel@orange.fr" class="icon-link">
          <img src="/src/assets/img/mail-icon.png" alt="Mail" class="icon" />
          <p class="icon-description">Mail</p>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LiensUtiles",
};
</script>

<style scoped>
/* Container général */
.liens-utiles-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  padding: 2rem;
  background-color: #f5f5f5;
}

/* Grille pour disposer les logos */
.grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* Deux colonnes pour une disposition plus compacte */
  grid-gap: 1.5rem;
  max-width: 600px;
  width: 100%;
  justify-items: center;
  text-align: center;
}

/* Conteneur des icônes */
.icon-container {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #eaeaea;
  border-radius: 12px;
  padding: 1rem;
  transition: transform 0.3s ease;
}

.icon-link {
  text-decoration: none;
  color: inherit;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

/* Icône individuelle */
.icon {
  width: 50px;
  height: 50px;
  margin-bottom: 0.5rem;
  transition: transform 0.3s ease;
}

/* Description sous chaque icône */
.icon-description {
  font-size: 1rem;
  font-weight: bold;
  margin: 0;
}

/* Effet de grossissement au survol */
.icon-container:hover {
  transform: scale(1.1);
}

.icon-container:hover .icon {
  animation: bounce 0.5s infinite;
}

/* Animation de sursaut */
@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-5px);
  }
}
</style>
