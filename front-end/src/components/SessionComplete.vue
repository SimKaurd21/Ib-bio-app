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
<style scoped>
div {
  min-height: 100vh;
  background: #edf7f0;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  padding: 30px;
  text-align: center;
}

h2 {
  color: #166534;
  font-size: 2.3rem;
  margin-bottom: 15px;
}

p {
  color: #6b7280;
  font-size: 1.1rem;
  margin: 8px 0;
}

button {
  width: 280px;

  padding: 14px 20px;
  margin-top: 15px;

  border-radius: 14px;
  border: none;

  cursor: pointer;

  font-size: 1rem;
  font-weight: 600;

  transition: 0.2s ease;

  background: white;
  color: #166534;

  border: 2px solid #dcfce7;
}

button:hover {
  transform: translateY(-3px);

  border-color: #22c55e;

  box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}

button:first-of-type {
  background: #22c55e;
  color: white;
}

button:first-of-type:hover {
  background: #16a34a;
}

button:last-of-type {
  background: #f3f4f6;
  color: #374151;
  border-color: #e5e7eb;
}

button:last-of-type:hover {
  background: #e5e7eb;
}
</style>