<script setup>
import {ref} from 'vue'

const form = ref({
  name: '',
  table: null,
  result: '',
})

const submitted = ref(false)
const submitResult = async () => {
}
</script>

<template>
  <div class="container w-full center-align">
    <div class="m-8 w-full justify-center">
      <h2>Inserisci Codice</h2>
      <form @submit.prevent="submitResult" class="space-y-4">
        <input
            v-model="form.code"
            type="text"
            id="code"
            required
            class="mt-1 block w-full px-3 py-2 border  rounded-lg shadow-sm"
        />
        <button type="submit"
                class="w-full font-semibold py-2 px-4 rounded-lg shadow">
          Invia Risultato
        </button>
      </form>
    </div>
  </div>
</template>

<style scoped>
</style>