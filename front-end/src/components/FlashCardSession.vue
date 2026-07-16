<template>
  <div class="container">
    <h1>IB Biology Recall</h1>
    <button @click="logout">
      Log Out
    </button>
    <button @click="goHome">
      Go Home
    </button>

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
import { cards } from '../data/cards'
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
      if (data.review_cards.includes(card.id)) {
        card.markedForReview = true
        reviewedCards.value.push(card.id)
      }
    })

  } catch (error) {
    console.error(error.message)
  }
}

async function nextCard() {
  await saveUserAnswer(
    props.userId,
    currentCard.value.id,
    userAnswer.value
  )

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
  await loadReviewCards()

  if (props.reviewMode) {
    studyCards.value = cards.filter(card =>
      reviewedCards.value.includes(card.id)
    )
  } else {
    studyCards.value = cards
  }

  currentIndex.value = 0
  currentCard.value = studyCards.value[0]

  await loadUserAnswer()
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
    console.error(error.message)
  }
}
</script>
