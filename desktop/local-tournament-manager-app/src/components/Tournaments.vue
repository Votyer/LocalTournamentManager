<script setup lang="ts">
import {onMounted, ref} from "vue";

const data = ref([])

onMounted(async () => {
  const res = await fetch(`http://localhost:8000/tournaments`, {
    method: 'GET',
    headers: {'Content-Type': 'application/json'},
  })
  const json = await res.json()
  console.log(data)
  data.value = json
})

</script>

<template>
  <div class="overflow-x-auto">
    <table class="min-w-full bg-white border border-gray-300 rounded-md shadow-sm">
      <thead class="bg-emerald-700 text-white">
      <tr>
        <th class="px-4 py-2 text-left">#</th>
        <th class="px-4 py-2 text-left">Nome</th>
        <th class="px-4 py-2 text-left">Codice</th>
        <th class="px-4 py-2 text-left">Giocatori</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(item, index) in data" :key="item.name" class="border-t">
        <td class="px-4 py-2">{{ index + 1 }}</td>
        <td class="px-4 py-2">{{ item.name }}</td>
        <td class="px-4 py-2">{{ item.code }}</td>
        <td class="px-4 py-2 capitalize">{{ item.players.length }}</td>
      </tr>
      </tbody>
    </table>
  </div>

</template>

<style scoped>

</style>