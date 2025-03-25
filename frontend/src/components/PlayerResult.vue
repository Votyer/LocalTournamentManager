<template>
  <div class="max-w-md mx-auto p-6 shadow-lg rounded-xl mt-10">
    <h2 class="text-2xl font-bold mb-4 text-center text-gray-800">Invia Risultato</h2>
    <form @submit.prevent="submitResult" class="space-y-4">
      <div>
        <label for="name" class="block text-sm font-medium text-gray-700">Nome Giocatore</label>
        <input
            v-model="form.name"
            type="text"
            id="name"
            required
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500"
        />
      </div>

      <div>
        <label for="table" class="block text-sm font-medium ">Tavolo</label>
        <input
            v-model.number="form.table"
            type="number"
            id="table"
            required
            min="1"
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500"
        />
      </div>

      <div>
        <label for="result" class="block text-sm font-medium text-gray-700">Risultato</label>
        <select
            v-model="form.result"
            id="result"
            required
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500"
        >
          <option value="" disabled selected>Seleziona un risultato</option>
          <option value="1">Vittoria</option>
          <option value="2">Sconfitta</option>
          <option value="0">Pareggio</option>
        </select>
      </div>

      <button
          type="submit"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-lg shadow"
      >
        Invia Risultato
      </button>
    </form>

    <div v-if="submitted" class="mt-4 text-green-600 text-center">
      ✅ Risultato inviato con successo!
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const form = ref({
  name: '',
  table: null,
  result: '',
})

const submitted = ref(false)

const submitResult = async () => {
  try {
    await fetch('http://localhost:8000/submitResult', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form.value),
    })

    submitted.value = true
    setTimeout(() => {
      submitted.value = false
      form.value = { name: '', table: null, result: '' }
    }, 3000)
  } catch (error) {
    console.error('Errore durante l’invio:', error)
  }
}
</script>
