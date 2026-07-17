<template>
    <div>
        <h1>Dashboard</h1>
        <p>Welcome to your dashboard!</p>

        <button @click="$emit('startSession')">
            Start New Session
        </button>
        <button @click="$emit('reviewCards')">
            Review Cards
        </button>
        <button @click="$emit('logout')">
            Log Out
        </button>

    </div>
</template>

<script setup>
defineEmits([
  "startSession",
  "reviewCards",
  "logout"
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
  padding: 20px;
}

h1 {
  color: #166534;
  font-size: 2.5rem;
  margin-bottom: 10px;
}

p {
  color: #6b7280;
  font-size: 1.1rem;
  margin-bottom: 35px;
}

button {
  width: 300px;
  padding: 15px;
  margin: 10px;
  border-radius: 14px;
  border: none;
  cursor: pointer;

  font-size: 1rem;
  font-weight: 600;

  background: white;
  color: #166534;

  border: 2px solid #dcfce7;

  transition: 0.2s ease;
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
  border-color: #d1d5db;
}
</style>