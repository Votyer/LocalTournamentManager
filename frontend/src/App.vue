<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import PlayerResult from "@/components/PlayerResult.vue";
import PlayerJoinTournament from "@/components/PlayerJoinTournament.vue";
</script>

<template>
  <main>
    <PlayerJoinTournament/>
    <PlayerResult/>
  </main>
</template>

<style scoped>
@import "tailwindcss";
</style>
