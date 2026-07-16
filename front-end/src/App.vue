<script setup>
import { ref, onMounted } from 'vue'
import AuthPage from './components/AuthPage.vue'
import FlashCardSession from './components/FlashCardSession.vue'
import Dashboard from './components/Dashboard.vue'
import { getReviewCards } from './services/api'

const loggedIn = ref(false)
const userId = ref(null)
const currentPage = ref("dashboard")

function handleLoginSuccess(id) {
  loggedIn.value = true
  userId.value = id
  currentPage.value = "dashboard"
  console.log("Current page:", currentPage.value)
  localStorage.setItem("userId", id)
}

function handleLogout() {
  loggedIn.value = false
  userId.value = null
  currentPage.value = "dashboard"

  localStorage.removeItem("userId")
}

async function startReviewSession() {
  try {
    const data = await getReviewCards(userId.value)

    if (data.review_cards.length === 0) {
      alert("You don't have any cards marked for review yet.")
      return
    }

    currentPage.value = "review"

  } catch (error) {
    console.error(error.message)
  }
}

onMounted(() => {
  const savedUserId = localStorage.getItem("userId")
  if (savedUserId) {
    loggedIn.value = true
    userId.value = Number(savedUserId)
  }
})
</script>

<template>
  <AuthPage
    v-if="!loggedIn"
    @loginSuccess="handleLoginSuccess"
  />

  <Dashboard
    v-else-if="currentPage === 'dashboard'"
    @startSession="currentPage = 'study'"
    @reviewCards="startReviewSession"
    @logout="handleLogout"
  />

  <FlashCardSession
    v-else
    :userId="userId"
    :reviewMode="currentPage === 'review'"
    @logout="handleLogout"
    @goHome="currentPage = 'dashboard'"
  />
</template>
