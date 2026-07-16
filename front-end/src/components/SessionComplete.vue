<template>
  <div>
    <h2>Session Complete!</h2>
    <p>
      You have reviewed {{ totalCards }} cards.
    </p>
    <p>
      You marked {{ reviewedCount }} cards for review.
    </p>
    <button
      v-if="reviewedCount > 0"
      @click="$emit('reviewMarkedCards')"
    >
      Review Marked Cards
    </button>

    <button @click="$emit('restartSession')">
      Restart Session
    </button>
  </div>
</template>

<script setup>
defineProps({
  totalCards: Number,
  reviewedCount: Number
})

defineEmits([
  "reviewMarkedCards",
  "restartSession"
])
</script>