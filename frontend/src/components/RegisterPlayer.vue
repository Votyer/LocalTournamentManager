<script setup>

import {ref} from "vue";
import {useRouter} from "vue-router";
import {usePlayerStore} from "@/stores/playerStore.js";

const playerStore = usePlayerStore()
const router = useRouter()
const form = ref({
  name: '',
  player_id: null
})
const submitted = ref(false)
const submitResult = async () => {
  playerStore.register_player(form.value)
  submitted.value = true
  await router.push(`/join-tournament`)
}
</script>

<template>
  <div class="w-full mx-auto">
    <h2>Register Player</h2>
    <form @submit.prevent="submitResult" class="py-2">
      <label for="name" class="block text-sm font-medium ">Nome Giocatore</label>
      <input
          v-model="form.name"
          type="text"
          id="name"
          required
          class="w-full py-2 px-4 border rounded-lg shadow-sm mt-2 mb-2"
      />
      <label for="player_id" class="block text-sm font-medium ">ID Giocatore</label>
      <input
          v-model="form.player_id"
          type="text"
          id="player_id"
          required
          class="w-full py-2 px-4 border rounded-lg shadow-sm mt-2 mb-2"
      />
      <button type="submit"
              class="w-full font-semibold py-2 px-4 rounded-lg shadow mt-2 mb-2 bg-blue-950">
        Invia Risultato
      </button>
    </form>
  </div>

</template>

<style scoped>

</style>