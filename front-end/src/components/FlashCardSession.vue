<template>
  <div class="container">
    <h1>IB Biology Recall</h1>

    <div v-if="sessionComplete">
      <h2>Session Complete!</h2>
      <p>You have reviewed {{ studyCards.length }} cards.</p>
      <p>You marked {{ reviewedCards.length }} cards for review.</p>
      <button v-if="reviewedCards.length > 0"
        @click="reviewMarkedCards">
        Review Marked Cards
      </button>
      <button @click="restartSession">
        Restart Session
      </button>
    </div>

    <div v-else>
    <Transition name="slide" mode="out-in">

    <div class="card" :key="currentCard.id">

      <div class="review">

      <p class="topic-title">{{ currentCard.topic }}</p>

      <button @click="markForReview">
        {{
          currentCard.markedForReview
          ? 'Unmark for Review'
          : 'Mark for Review'
        }}
      </button>

    </div>
      <div class="question-box">
        <h2>{{ currentCard.question }}</h2>
      </div>

      <textarea 
      v-model="userAnswer"
      placeholder="Type your answer here..."
      rows="6">
      </textarea>

      <div v-if="showAnswer" class="answer-box">
        <h3>Answer</h3>
        <p>{{ currentCard.answer }}</p>
      </div>

      <div class="button-row">
      <button @click="prevCard" class="prev-button">
          Previous Card
        </button>

        <button @click="toggleAnswer">
         {{ showAnswer ? 'Hide Answer' : 'Reveal Answer' }}
        </button>

        <button @click="nextCard" class="next-button">
          Next Card
        </button> 
       </div>
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
    </Transition>
  </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { cards } from '../data/cards'
import { 
  saveReview,
  getReviewCards,
  deleteReviewCard
} from '../services/api'

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
  }
})

async function loadReviewCards() {
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

function nextCard() {
  showAnswer.value = false
  userAnswer.value = ''
  currentIndex.value++

  if (currentIndex.value >= studyCards.value.length) {
    sessionComplete.value = true
    return
  }

  currentCard.value = studyCards.value[currentIndex.value]
}

function prevCard() {
  showAnswer.value = false
  userAnswer.value = ''
  currentIndex.value--

  if (currentIndex.value < 0) {
    currentIndex.value = studyCards.value.length - 1
  }

  currentCard.value = studyCards.value[currentIndex.value]
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

function restartSession() {
  studyCards.value = cards
  sessionComplete.value = false
  currentIndex.value = 0
  currentCard.value = studyCards.value[0]
  showAnswer.value = false
  userAnswer.value = ''
}

function reviewMarkedCards() { 
  studyCards.value = cards.filter(card =>
    reviewedCards.value.includes(card.id)
  )

  sessionComplete.value = false
  currentIndex.value = 0
  currentCard.value = studyCards.value[0]
  showAnswer.value = false
  userAnswer.value = ''
}

onMounted(() => {
  loadReviewCards()
})
</script>
