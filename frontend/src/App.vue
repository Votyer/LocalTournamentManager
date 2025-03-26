<script setup>
import {useRouter} from "vue-router";
import {usePlayerStore} from "@/stores/playerStore.js";

const playerStore = usePlayerStore()
const router = useRouter()

if (!playerStore.player_id || !playerStore.name) {
  //navigate to join tournament
  router.push('/register-player')
}

</script>

<template>
  <main>
    <div class="col">
      <RouterView/>
    </div>
  </main>
</template>

<style scoped>
</style>
