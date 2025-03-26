<template>
  <div class="max-w-md mx-auto p-6 shadow-lg rounded-xl mt-10">
    <h2 class="text-4xl font-bold mb-4 text-center">Tavolo {{currentTable}}</h2>
    <div class="grid gap-6">
      <button class="bg-green-500 hover:bg-green-900 text-white py-2 px-5 rounded-4xl">Vittoria</button>
      <button class="bg-white hover:bg-gray-500 py-2 px-5 rounded-4xl text-gray-700">Pareggio</button>
      <button class="bg-red-500 hover:bg-red-900 text-white py-2 px-5 rounded-4xl">Sconfitta</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import {useRouter} from "vue-router";

const form = ref({
  name: '',
  table: null,
  result: '',
})

const submitted = ref(false)
const route = useRouter()

const currentTable = route.currentRoute.value.params.table
console.log(currentTable)
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
