<script setup>
import {ref} from 'vue'
import {useTournamentStore} from '@/stores/tournamentStore'
import AlertMessage from "@/components/AlertMessage.vue";
import {usePlayerStore} from "@/stores/playerStore.js";
import {useRouter} from "vue-router";

const playerStore = usePlayerStore()
const tournamentStore = useTournamentStore()
const router = useRouter()
const form = ref({
  code: '',
})

const submitted = ref(false)
let errorMessage = ref(null)
const submitResult = async () => {
  try {
    errorMessage.value = null
    const tournamentCode = form.value.code
    const res = await fetch(`http://localhost:8000/joinTournament?code=${tournamentCode}`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        name: playerStore.name,
        player_id: playerStore.player_id,
      }),
    })

    const data = await res.json()

    if (!res.ok) {
      throw new Error(data.error || 'Something went wrong')
    }

    tournamentStore.setTournament(data)
    router.push('/')
    setTimeout(() => {
      submitted.value = false
      form.value = {name: '', table: null, result: ''}
    }, 3000)
  } catch (error) {
    console.error('Errore durante l’invio:', error)
    errorMessage.value = error.message
  }
}
</script>

<template>
  <div class="container w-full center-align">
    <div class="w-full justify-center">
      <h2>Inserisci Codice</h2>
      <form @submit.prevent="submitResult" class="space-y-4">
        <input
            v-model="form.code"
            type="text"
            id="code"
            required
            class="mt-1 w-full px-3 py-2 border  rounded-lg shadow-sm"
        />
        <button type="submit"
                class="w-full font-semibold py-2 px-4 rounded-lg shadow bg-emerald-900">
          Partecipa
        </button>
      </form>
      <AlertMessage v-if="errorMessage" :message="errorMessage" type="error"/>
    </div>
  </div>
</template>

<style scoped>
</style>