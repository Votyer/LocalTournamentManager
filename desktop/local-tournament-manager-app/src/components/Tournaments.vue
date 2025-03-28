<script setup lang="ts">
import {onMounted, ref} from "vue";
import CreateTournamentDialog from "./CreateTournamentDialog.vue";

const data = ref([])

onMounted(async () => loadData())

const loadData = async () => {
  const res = await fetch(`http://localhost:8000/tournaments`, {
    method: 'GET',
    headers: {'Content-Type': 'application/json'},
  })
  const json = await res.json()
  console.log(data)
  data.value = json
}

const showDialog = ref(false)

const onTournamentCreated = (tournament) => loadData()

function createTournament() {
  showDialog.value = true
}

</script>

<template>
  <div class="overflow-x-auto">
    <button @click="createTournament()" class="bg-emerald-700 hover:bg-emerald-900 text-white rounded-xl px-5 py-3 md-11">Crea Torneo</button>
    <CreateTournamentDialog v-if="showDialog" @close="showDialog = false" @created="onTournamentCreated" />
    <table class="min-w-full bg-white border border-gray-300 rounded-md shadow-sm mt-5">
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