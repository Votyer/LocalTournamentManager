<template>
  <div class="flex items-center gap-2 text-sm">
    <span
        :class="[
        'w-3 h-3 rounded-full',
        status === 'online' ? 'bg-green-500' : 'bg-red-500'
      ]"
    ></span>
    <span class="text-white">
      Server: <strong>{{ status }}</strong>
    </span>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const status = ref<'online' | 'offline'>('offline')

const checkServer = async () => {
  try {
    const res = await fetch('http://localhost:8000/', { method: 'GET' })
    status.value = res.ok ? 'online' : 'offline'
  } catch {
    status.value = 'offline'
  }
}

// check subito al mount
onMounted(() => {
  checkServer()
  // ripeti ogni 10 secondi
  setInterval(checkServer, 10000)
})
</script>
