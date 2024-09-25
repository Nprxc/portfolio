<template>
  <div class="competences-wrapper">
    <h1 class="title">Mes compétences</h1>
    <div class="competences-container">
      <div class="grid">
        <div class="competence" v-for="(competence, index) in competences" :key="index">
          <img v-if="competence.image" :src="competence.image" :alt="competence.name" class="competence-logo" />
          <p v-else>{{ competence.name }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      competences: [
        {name: "JavaScript", image: "/src/assets/img/javascript-logo.webp"},
        {name: "VueJS", image: "/src/assets/img/vue-logo.png"},
        {name: "Java", image: "/src/assets/img/java-logo.webp"},
        {name: "Spring", image: "/src/assets/img/spring-logo.png"},
        {name: "MySQL", image: "/src/assets/img/mysql-logo.png"},
        {name: "Docker", image: "/src/assets/img/docker-logo.jpg"},
        {name: "Git", image: "/src/assets/img/git-logo.png"},
        {name: "React", image: "/src/assets/img/react-logo.png"},
        {name: "Azure", image: "/src/assets/img/azure-logo.png"},
      ],
    };
  },
};
</script>

<style scoped>
/* Conteneur général */
.competences-wrapper {
  padding: 2rem;
  background-color: white;
  text-align: center;
}

/* Titre */
.title {
  font-size: 2.5rem;
  color: #2d3436;
  margin-bottom: 3rem;
  animation: fadeInTitle 1.5s ease-in-out;
}

/* Conteneur des compétences */
.competences-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

/* Grille des compétences */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); /* Ajuste selon la taille de l'écran */
  grid-gap: 2rem;
  max-width: 1000px;
  width: 100%;
}

/* Chaque compétence */
.competence {
  background-color: #f4f4f4;
  padding: 2rem;
  border-radius: 15px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

.competence:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1); /* Ombre douce au survol */
}

/* Taille des logos de compétence */
.competence-logo {
  width: 100px;
  height: 100px;
  object-fit: contain; /* S'assure que les images gardent leurs proportions */
  margin-bottom: 1rem;
}

/* Style du texte sous les logos */
p {
  font-size: 1.3rem;
  font-weight: bold;
  color: #2d3436;
  margin: 0;
}

/* Animation d'apparition */
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
</style>
