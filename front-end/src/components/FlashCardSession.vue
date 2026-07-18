<template>
  <div class="container">
    <div v-if="loading" class='loading-screen'>
    <div class="spinner"></div>
      <h2>Loading your flashcards...</h2>
      <p>Preparing your study session...</p>
  </div>

  <div v-else-if="errorMessage" class="error-screen">
      <h2>Something went wrong</h2>
      <p>{{ errorMessage }}</p>

      <button @click="window.location.reload()">
       Try Again
      </button>
  </div>
      <div class="Top-buttons">
        <button @click="logout">
          Log Out
        </button>
        <button @click="goHome">
          Go Home
        </button>
      </div>
    <p v-if="saving" class="saving">
      Saving...
    </p>
    <p v-if="savedMessage" class="saved">
      Saved ✓
    </p>

    <SessionComplete
      v-if="sessionComplete"
      :totalCards="studyCards.length"
      :reviewedCount="reviewedCards.length"
      @reviewMarkedCards="reviewMarkedCards"
      @restartSession="restartSession"
    />

    <div v-else>
    <Transition name="slide" mode="out-in">

       <FlashCard
        :key="currentCard.id"
        :currentCard="currentCard"
        :showAnswer="showAnswer"
        :userAnswer="userAnswer"
        :saving="saving"

        @nextCard="nextCard"
        @prevCard="prevCard"
        @toggleAnswer="toggleAnswer"
        @markForReview="markForReview"
        @update:userAnswer="userAnswer = $event"/>
    
    </Transition>
       <div class="progress-bar">
        <div
          class="progress-fill"
            :style="{ width: ((currentIndex + 1) / studyCards.length) * 100 + '%' }"
        ></div>
        </div>

       <p class="progress">
        Card {{ currentIndex + 1 }} of {{ studyCards.length }}
       </p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import {cards} from '../data/cards'
import { 
  saveReview,
  getReviewCards,
  deleteReviewCard,
  saveUserAnswer,
  getUserAnswers
} from '../services/api'
import SessionComplete from "./SessionComplete.vue"
import FlashCard from "./FlashCard.vue"

const showAnswer = ref(false)
const currentIndex = ref(0)
const userAnswer = ref('')
const studyCards = ref(cards)
const currentCard = ref(studyCards.value[currentIndex.value])
const sessionComplete = ref(false)
const loading = ref(true)
const errorMessage = ref('')
const saving = ref(false)
const savedMessage = ref(false)

const reviewedCards = ref([])

const props = defineProps({
  userId: {
    type: Number,
    required: true
  },
  reviewMode: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(["logout", "goHome"])

function logout() {
  localStorage.removeItem("userId")
  emit("logout")
}

function goHome() {
  emit("goHome")
}

async function loadReviewCards() {
  reviewedCards.value = []
  try {
    const data = await getReviewCards(props.userId)

    studyCards.value.forEach(card => {
      card.markedForReview = data.review_cards.includes(card.id)

      if (card.markedForReview) {
      reviewedCards.value.push(card.id)
    }
    })

  } catch (error) {
    console.error(error.message)
  }
}

async function nextCard() {
   saving.value = true
   savedMessage.value = false

  try {
    await saveUserAnswer(
      props.userId,
      currentCard.value.id,
      userAnswer.value
    )

    savedMessage.value = true
    setTimeout(() => {
      savedMessage.value = false
    }, 2000)

  } catch(error) {
    errorMessage.value = "Could not save answer."

  } finally {
    saving.value = false
  }
  showAnswer.value = false
  currentIndex.value++

  if (currentIndex.value >= studyCards.value.length) {
    sessionComplete.value = true
    return
  }
  currentCard.value = studyCards.value[currentIndex.value]
  await loadUserAnswer()
}

async function prevCard() {
  showAnswer.value = false

  currentIndex.value--

  if (currentIndex.value < 0) {
    currentIndex.value = studyCards.value.length - 1
  }

  currentCard.value = studyCards.value[currentIndex.value]

  await loadUserAnswer()
}

async function markForReview() {
  const id = currentCard.value.id
  currentCard.value.markedForReview = !currentCard.value.markedForReview

  if (currentCard.value.markedForReview) {

    if (!reviewedCards.value.includes(id)) {
      reviewedCards.value.push(id)

      try {
        await saveReview(props.userId, id)
      } catch (error) {
        console.error(error.message)
      }
    }
  } else {
    reviewedCards.value = reviewedCards.value.filter(
    cardId => cardId !== id
  )

  try {
    await deleteReviewCard(props.userId, id)
  } catch (error) {
    console.error(error.message)
  }
  }
}

function toggleAnswer() {
  showAnswer.value = !showAnswer.value
}

async function restartSession() {
  studyCards.value = cards
  sessionComplete.value = false
  currentIndex.value = 0
  currentCard.value = studyCards.value[0]
  showAnswer.value = false

  await loadUserAnswer()
}

async function reviewMarkedCards() { 

  if (reviewedCards.value.length === 0) {
    alert("You haven't marked any cards for review yet.")
    return
  }

  studyCards.value = cards.filter(card =>
    reviewedCards.value.includes(card.id)
  )

  sessionComplete.value = false
  currentIndex.value = 0
  currentCard.value = studyCards.value[0]
  showAnswer.value = false

  await loadUserAnswer()
}

onMounted(async () => {
  try {
    await loadReviewCards()

    if (props.reviewMode) {
      studyCards.value = cards.filter(card =>
        reviewedCards.value.includes(card.id)
      )
    } else {
      studyCards.value = cards
    }

    currentIndex.value = 0

    if (studyCards.value.length === 0) {
      loading.value = false
      return
    }

    currentCard.value = studyCards.value[0]
    await loadUserAnswer()

  } catch (error) {
    errorMessage.value = "Unable to load your study session."

  } finally {
    loading.value = false
  }
})

async function loadUserAnswer() {
  try {
    const data = await getUserAnswers(
      props.userId,
      currentCard.value.id
    )

    userAnswer.value = data.answer

  } catch (error) {
    // If no answer exists yet, keep textarea empty
    userAnswer.value = ''
    if (error.message !== "No answer found") {
      console.error(error.message)
    }
  }
}
</script>
<style scoped>
.loading-screen {
  min-height: 70vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.loading-screen h2 {
  margin-top: 20px;
  font-size: 1.8rem;
}

.loading-screen p {
  margin-top: 8px;
  color: #666;
}

.spinner {
  width: 45px;
  height: 45px;
  border: 5px solid #d8f3dc;
  border-top: 5px solid #2d6a4f;
  border-radius: 50%;
  animation: spin 0.9s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
}
.saving,
.saved {
  margin-top: 10px;
  font-size: 0.95rem;
}
.saved {
  color: #2d6a4f;
}
.top-buttons {
  display: flex;
  gap: 10px;
  justify-content: center;
  margin-bottom: 20px;
}
</style>
