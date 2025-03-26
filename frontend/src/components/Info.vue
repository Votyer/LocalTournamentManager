<script setup>
import {useTournamentStore} from "@/stores/tournamentStore.js";
import {usePlayerStore} from "@/stores/playerStore.js";

const tournamentStore = useTournamentStore()
const playerStore = usePlayerStore()
</script>

<template>
  <div class="container w-full bg-emerald-900"></div>
  <div class="w-full justify-center mx-auto">
    <p>Tournament: {{tournamentStore.name}}</p>
    <p>Player: {{playerStore.name}}</p>
    <p>Player Id: {{playerStore.player_id}}</p>
  </div>
</template>

<style scoped>

</style>