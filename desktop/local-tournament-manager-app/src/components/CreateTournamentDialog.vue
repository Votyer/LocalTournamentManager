<template>
  <div v-if="visible" class="fixed inset-0  bg-opacity-50 flex items-center justify-center z-50">
    <div class="bg-white rounded-lg shadow-lg p-6 w-full max-w-md">
      <h2 class="text-xl font-semibold mb-4 text-emerald-800">Crea Torneo</h2>

      <form @submit.prevent="submit">
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700">Nome Torneo</label>
          <input v-model="form.name" type="text" required class="w-full px-3 py-2 border rounded-lg" />
        </div>

        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700">Tavoli (es: 1,2,3)</label>
          <input v-model="form.tables" type="text" required class="w-full px-3 py-2 border rounded-lg" />
        </div>

        <div class="flex justify-end space-x-2 mt-4">
          <button type="button" @click="$emit('close')" class="px-4 py-2 bg-gray-300 rounded">Annulla</button>
          <button type="submit" class="px-4 py-2 bg-emerald-700 text-white rounded">Crea</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits(['close', 'created'])

const form = ref({
  name: '',
  tables: '',
  max_players: 30,
})

const visible = defineModel({ default: true })

const submit = async () => {
  const payload = {
    name: form.value.name,
    tables: form.value.tables.split(',').map(t => parseInt(t.trim())),
    max_players: form.value.max_players,
    players: []
  }

  try {
    const res = await fetch('http://localhost:8000/createTournament', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })

    if (!res.ok) {
      const err = await res.json()
      throw new Error(err.detail || 'Errore creazione torneo')
    }

    emit('created', await res.json())
    emit('close')
  } catch (error) {
    console.error('Errore:', error.message)
    alert(error.message)
  }
}
</script>
