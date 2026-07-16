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