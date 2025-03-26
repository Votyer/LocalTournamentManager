import {createRouter, createWebHistory} from 'vue-router'
import RegisterPlayer from "@/components/RegisterPlayer.vue";
import PlayerJoinTournament from "@/components/PlayerJoinTournament.vue";
import Home from "@/components/Home.vue";
import PlayerResult from "@/components/PlayerResult.vue";

const routes = [
    {path: '/register-player', name: 'register-player', component: RegisterPlayer},
    {path: '/join-tournament', name: 'join-tournament', component: PlayerJoinTournament},
    {path: '/payer-result/:table', name: 'payer-result', component: PlayerResult},
    {path: '/', name: 'home', component: Home},
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
