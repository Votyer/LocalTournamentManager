<template>
  <div
      v-if="visible"
      :class="[
      'px-4 py-2 rounded-md mb-4 border shadow-sm',
      typeClass
    ]"
  >
    {{ message }}
  </div>
</template>

<script setup>
import { computed, watch, ref } from 'vue'
import { defineProps } from 'vue'

const props = defineProps({
  message: String,
  type: {
    type: String,
    default: 'error', // "success", "info"
  },
  autoHide: {
    type: Boolean,
    default: true
  },
  duration: {
    type: Number,
    default: 4000 // ms
  }
})

const visible = ref(!!props.message)

watch(() => props.message, (newVal) => {
  visible.value = !!newVal

  if (props.autoHide && newVal) {
    setTimeout(() => {
      visible.value = false
    }, props.duration)
  }
})

const typeClass = computed(() => {
  switch (props.type) {
    case 'success':
      return 'bg-green-100 border-green-400 text-green-700'
    case 'info':
      return 'bg-blue-100 border-blue-400 text-blue-700'
    default:
      return 'bg-red-100 border-red-400 text-red-700'
  }
})
</script>
