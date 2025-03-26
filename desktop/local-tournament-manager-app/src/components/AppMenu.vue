<template>
  <nav class="bg-emerald-800 text-white px-4 py-3 shadow-md">
    <div class="flex items-center justify-between">
      <div class="text-xl font-semibold">LocalTournamentManager</div>
      <ul class="flex space-x-4 text-sm">
        <li><router-link to="/" class="hover:underline">Home</router-link></li>
        <li><router-link to="/submit" class="hover:underline">Invia Risultato</router-link></li>
        <li><router-link to="/admin" class="hover:underline">Gestione</router-link></li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
.router-link-active {
  font-weight: bold;
  text-decoration: underline;
}
</style>
