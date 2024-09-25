<template>
  <div class="container-fluid d-flex align-items-center justify-content-center vh-100 qui-suis-je-wrapper">
    <div class="text-center">
      <!-- Conteneur pour la photo -->
      <div class="photo-container mx-auto">
        <img src="" alt="Axel Guy" class="photo img-fluid rounded-circle" />
      </div>
      <!-- Titre de la section -->
      <h1 class="mt-3">Qui suis-je ?</h1>
      <!-- Texte de présentation -->
      <p class="introduction">
        Futur ingénieur généraliste spécialisé en cybersécurité, je cherche à contribuer à la création d'un environnement numérique sûr et fiable.
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "QuiSuisJe",
};
</script>

<style scoped>
/* Conteneur principal pour centrer le contenu */
.qui-suis-je-wrapper {
  background-color: #ffffff; /* Fond doux et lumineux */
  padding: 2rem;
}

/* Conteneur pour la photo avec bordure */
.photo-container {
  width: 180px;
  height: 180px;
  border: 4px solid #00b894; /* Bordure verte légère */
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* Légère ombre portée */
  transition: transform 0.3s ease-in-out;
}

.photo-container:hover {
  transform: scale(1.05); /* Zoom léger au survol */
}

/* Photo ajustée pour bien s'intégrer dans le cercle */
.photo {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Style du titre avec animation */
h1 {
  font-size: 2.5rem;
  color: #2d3436; /* Couleur sombre pour contraste */
  margin-top: 1.5rem;
  animation: fadeInTitle 1.5s ease-in-out;
}

/* Animation pour le texte */
.introduction {
  font-size: 1.2rem;
  color: #636e72; /* Couleur de texte douce */
  max-width: 600px;
  margin: 1.5rem auto;
  line-height: 1.6;
  animation: fadeInText 2s ease-in-out;
}

/* Animation d'apparition pour le titre */
@keyframes fadeInTitle {
  0% {
    opacity: 0;
    transform: translateY(-30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Animation d'apparition pour le texte */
@keyframes fadeInText {
  0% {
    opacity: 0;
    transform: translateY(30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
