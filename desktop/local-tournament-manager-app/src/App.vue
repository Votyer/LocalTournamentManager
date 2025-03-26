<script setup lang="ts">
import AppMenu from "./components/AppMenu.vue";
</script>

<template>
  <div class="min-h-screen bg-gray-100">
    <AppMenu/>
    <main class="p-4">
      <Router-View/>
    </main>
  </div>
</template>

<style scoped>

</style>