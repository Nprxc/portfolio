<template>
  <div id="title">
    <h1 class="title">Mes expériences Pro</h1>
  </div>
  <div class="experiences-container">
    <!-- Affichage de la grille initiale avec les expériences -->
    <div class="grid" v-if="!showDetails">
      <div
          v-for="(experience, index) in experiences"
          :key="index"
          class="experience-card"
          @click="openDetails(experience)"
      >
        <h3>{{ experience.title }}</h3>
        <p>{{ experience.shortDescription }}</p>
        <span>{{ experience.dates }}</span>
      </div>
    </div>

    <!-- Affichage des détails de l'expérience lorsque l'on clique sur une carte -->
    <div v-if="showDetails" class="experience-details">
      <div class="details-header">
        <h2>{{ currentExperience.title }}</h2>
        <p>{{ currentExperience.dates }}</p>
      </div>
      <div class="details-body">
        <div class="image-grid">
          <img v-for="(image, index) in currentExperience.images" :key="index" :src="image" alt="Experience image" />
        </div>
        <div class="description-box">
          <!-- Utilisation de v-html pour rendre le contenu HTML -->
          <p v-html="currentExperience.fullDescription"></p>
        </div>
      </div>
      <button @click="closeDetails">Retour</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showDetails: false, // Pour savoir si on affiche la page de détails
      currentExperience: null, // Expérience actuelle sélectionnée
      experiences: [
        {
          title: "Stage Cybersécurité Web",
          shortDescription: "Pentest et devOps chez NEVER2WAIT.",
          dates: "02 Mai 2024 - 02 Août 2024",
          fullDescription: `
            Durant ce stage chez NEVER2WAIT, j'ai mené plusieurs missions :
            <ul>
              <li>Pentest d'applications web et Active Directory</li>
              <li>Consultations en cybersécurité</li>
              <li>Architecture Réseaux et DevOps sur Microsoft Azure</li>
              <li>Développement web avec Symfony et React</li>
            </ul>
          `,
          images: ["img_never2wait1.jpg", "img_never2wait2.jpg", "img_never2wait3.jpg", "img_never2wait4.jpg"],
        },
        {
          title: "Consultant Sécurité Web Junior",
          shortDescription: "Réalisation et gestion du site web pour ANI AMIS.",
          dates: "Septembre 2018 - Présent",
          fullDescription: `
            En tant que consultant sécurité web pour l'entreprise Cadeaux Photos, j'ai été en charge des missions suivantes :
            <ul>
              <li>Réalisation de l'infrastructure du site web</li>
              <li>Administration des serveurs et des réseaux</li>
              <li>Pentest / Audit de sécurité application web</li>
              <li>Planification de la politique de sécurité</li>
              <li>Transfert / Migration des données vers un autre hébergement</li>
            </ul>
          `,
          images: ["img_aniamis1.jpg", "img_aniamis2.jpg", "img_aniamis3.jpg", "img_aniamis4.jpg"],
        },
        {
          title: "Contrat Pro Développeur Fullstack",
          shortDescription: "Développeur Fullstack chez UNIS.",
          dates: "02 septembre 2024 - Présent",
          fullDescription: `
            En tant que Développeur Fullstack, j'ai participé au développement et à la refonte d'une solution Intranet pour la gestion des processus de l'entreprise.
            <ul>
              <li>Audit fonctionnel et technique de la solution Intranet existante</li>
              <li>Préconisations pour la refonte de l'application</li>
              <li>Développement dans un environnement technique complexe utilisant Java JEE, Spring, MyBatis, et VueJS</li>
              <li>Participation au développement de micro-services expérimentaux tels que API Gateway, Service Discovery, et Cloud</li>
              <li>Support applicatif des applications Intranet/Internet</li>
            </ul>
          `,
          images: ["img_fullstack1.jpg", "img_fullstack2.jpg", "img_fullstack3.jpg", "img_fullstack4.jpg"],
        },
      ],
    };
  },
  methods: {
    openDetails(experience) {
      this.currentExperience = experience;
      this.showDetails = true;
    },
    closeDetails() {
      this.showDetails = false;
    },
  },
};
</script>

<style scoped>
/* Titre principal */
.title {
  font-size: 2.5rem;
  color: #2d3436;
  margin-bottom: 3rem;
  text-align: center;
  animation: fadeInTitle 1.5s ease-in-out;
}

/* Grille d'expérience */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  padding: 2rem;
}

.experience-card {
  background-color: #f0f0f0;
  padding: 1.5rem;
  border-radius: 10px;
  cursor: pointer;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.experience-card:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.experience-card h3 {
  margin-bottom: 1rem;
  color: #2d3436;
}

.experience-card p {
  margin-bottom: 0.5rem;
  color: #636e72;
}

.experience-card span {
  font-size: 0.9rem;
  color: #b2bec3;
}

/* Style de la vue détaillée */
.experience-details {
  background-color: white;
  padding: 2rem;
  max-width: 80%;
  margin: 2rem auto;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  animation: fadeInDetails 1s ease-in-out;
}

.details-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.details-header h2 {
  font-size: 2.5rem;
  margin: 0;
  color: #2d3436;
}

.details-body {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 20px;
}

.image-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
}

.image-grid img {
  width: 150px; /* Largeur fixe pour les images */
  height: 150px; /* Hauteur fixe pour les images */
  border-radius: 8px;
  object-fit: cover; /* Permet de garder les proportions sans déformation */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Ombre douce */
}


.description-box {
  background-color: #f9f9f9;
  padding: 1.5rem;
  border-radius: 8px;
}

/* Bouton de retour */
button {
  margin-top: 1rem;
  padding: 0.75rem 1.5rem;
  background-color: #00b894;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

button:hover {
  background-color: #55efc4;
  transform: scale(1.05);
}

/* Animations */
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

@keyframes fadeInDetails {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
