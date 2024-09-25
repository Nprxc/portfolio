import Vue from 'vue';
import Router from 'vue-router';
import QuiSuisJe from './components/QuiSuisJe.vue';
import ParcoursAcademique from './components/ParcoursAcademique.vue';
import ExperiencesPro from './components/ExperiencesPro.vue';
import Competences from './components/Competences.vue';
import LiensUtiles from './components/LiensUtiles.vue';

Vue.use(Router);

export default new Router({
    routes: [
        { path: '/', component: QuiSuisJe },
        { path: '/parcours-academique', component: ParcoursAcademique },
        { path: '/experiences-pro', component: ExperiencesPro },
        { path: '/competences', component: Competences },
        { path: '/liens-utiles', component: LiensUtiles },
    ]
});
