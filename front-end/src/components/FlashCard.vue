<template>
  <div class="card">
    <div class="review">
      <p class="topic-title">{{ currentCard.topic }}</p>

      <button @click="$emit('markForReview')">
        {{
          currentCard.markedForReview
            ? "Unmark for Review"
            : "Mark for Review"
        }}
      </button>
    </div>

    <div class="question-box">
      <h2>{{ currentCard.question }}</h2>
    </div>

    <textarea
      :value="userAnswer"
      @input="$emit('update:userAnswer', $event.target.value)"
      placeholder="Type your answer here..."
      rows="6"
    />

    <div v-if="showAnswer" class="answer-box">
      <h3>Answer</h3>
      <p>{{ currentCard.answer }}</p>
    </div>

    <div class="button-row">
      <button
        class="prev-button"
        @click="$emit('prevCard')"
      >
        Previous Card
      </button>

      <button @click="$emit('toggleAnswer')">
        {{ showAnswer ? "Hide Answer" : "Reveal Answer" }}
      </button>

      <button
        class="next-button"
        @click="$emit('nextCard')"
      >
        Next Card
      </button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  currentCard: Object,
  showAnswer: Boolean,
  userAnswer: String
})

defineEmits([
  "nextCard",
  "prevCard",
  "toggleAnswer",
  "markForReview",
  "update:userAnswer"
])
</script>