<template>
  <SignupForm />
  <div class="container">
    <h1>IB Biology Recall</h1>

    <div v-if="sessionComplete">
      <h2>Session Complete!</h2>
      <p>You have reviewed {{ cards.length }} cards.</p>

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
      <h2>{{ currentCard.question }}</h2>

      <textarea 
      v-model="userAnswer"
      placeholder="Type your answer here..."
      rows="6">
      </textarea>

      <p v-if="showAnswer">
        {{ currentCard.answer }}
      </p>

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
       <p class="progress">
        Card {{ currentIndex + 1 }} of {{ cards.length }}
       </p>
    </div>
    </Transition>
  </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { cards } from '../data/cards'

const showAnswer = ref(false)

const currentIndex = ref(0)

const userAnswer = ref('')

const currentCard = ref(cards[currentIndex.value])

const reviewCards = ref([])

const sessionComplete = ref(false)

function nextCard() {
  showAnswer.value = false
  userAnswer.value = ''
  currentIndex.value++

  if (currentIndex.value >= cards.length) {
    sessionComplete.value = true
    return
  }

  currentCard.value = cards[currentIndex.value]
}

function prevCard() {
  showAnswer.value = false
  userAnswer.value = ''
  currentIndex.value--

  if (currentIndex.value < 0) {
    currentIndex.value = cards.length - 1
  }

  currentCard.value = cards[currentIndex.value]
}

function markForReview(){
  currentCard.value.markedForReview =
  !currentCard.value.markedForReview
}

function toggleAnswer() {
  showAnswer.value = !showAnswer.value
}

function restartSession() {
  sessionComplete.value = false
  currentIndex.value = 0
  currentCard.value = cards[0]
}

</script>
