<script setup>
import { ref, onMounted } from 'vue'
import AuthPage from './components/AuthPage.vue'
import FlashCardSession from './components/FlashCardSession.vue'
import Dashboard from './components/Dashboard.vue'
import TopicSelection from './components/TopicSelection.vue'
import { getReviewCards } from './services/api'
import { Analytics } from "@vercel/analytics/vue"

const loggedIn = ref(false)
const userId = ref(null)
const currentPage = ref("dashboard")
const selectedDeck = ref(null)

function handleLoginSuccess(id) {
  loggedIn.value = true
  userId.value = id
  currentPage.value = "dashboard"
  localStorage.setItem("userId", id)
}

function handleLogout() {
  loggedIn.value = false
  userId.value = null
  currentPage.value = "dashboard"
  selectedDeck.value = null

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

function handleDeckSelection(deck) {
  selectedDeck.value = deck
  currentPage.value = "study"
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
    @startSession="currentPage = 'selectDeck'"
    @reviewCards="startReviewSession"
    @logout="handleLogout"
  />

  <TopicSelection
    v-else-if="currentPage === 'selectDeck'"
    @selectDeck="handleDeckSelection"
    @goHome="currentPage = 'dashboard'"
  />

  <FlashCardSession
    v-else
    :userId="userId"
    :deck="selectedDeck"
    :reviewMode="currentPage === 'review'"
    @logout="handleLogout"
    @goHome="currentPage = 'dashboard'"
  />
</template>