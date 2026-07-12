<script setup>
  import { ref } from 'vue'
  import AuthPage from './components/AuthPage.vue'
  import FlashCardSession from './components/FlashCardSession.vue'
  const loggedIn = ref(false)
</script>

<template>
  <AuthPage 
  v-if="!loggedIn" 
  @loginSuccess="loggedIn = true"
  />
  <FlashCardSession
    v-else
  />
</template>
