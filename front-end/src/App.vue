<script setup>
import { ref } from 'vue'
import AuthPage from './components/AuthPage.vue'
import FlashCardSession from './components/FlashCardSession.vue'

const loggedIn = ref(false)
const userId = ref(null)

function handleLoginSuccess(id) {
  loggedIn.value = true
  userId.value = id
}
</script>

<template>
  <AuthPage
    v-if="!loggedIn"
    @loginSuccess="handleLoginSuccess"
  />
  <FlashCardSession
    v-else
    :userId="userId"
  />
</template>
