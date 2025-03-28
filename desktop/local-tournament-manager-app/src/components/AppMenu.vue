<template>
  <nav class="bg-emerald-800 text-white px-4 py-3 shadow-md">
    <div class="flex items-center justify-between">
      <div class="text-xl font-semibold"><router-link to="/" class="hover:underline">LocalTournamentManager</router-link></div>
      <div class="flex space-x-4 text-sm">
        <ServerStatus/>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.router-link-active {
  font-weight: bold;
  text-decoration: underline;
}
</style>
<script setup lang="ts">
import ServerStatus from "./ServerStatus.vue";
</script>