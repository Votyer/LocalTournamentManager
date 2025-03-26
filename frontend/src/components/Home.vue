<script setup>
import {useTournamentStore} from "@/stores/tournamentStore.js";
import Info from "@/components/Info.vue";
import {useRouter} from "vue-router";

const tournamentStore = useTournamentStore()
const router = useRouter()

function selectTable(selTable) {
  //open
  router.push({name: "payer-result", params: {table: selTable}});
}
</script>

<template>
  <div class='container md-8'>
    <Info></Info>
  </div>
  <div class="container mt-8">
    <h6>Tavoli</h6>
    <div class="grid grid-cols-2 gap-4 content-center">
      <button v-for="table in tournamentStore.tables" @click="selectTable(table)"
              class="bg-cyan-900 hover:bg-cyan-950 rounded-xl py-1.5 px-15 m-6">{{ table }}
      </button>
    </div>
  </div>
</template>

<style scoped>

</style>