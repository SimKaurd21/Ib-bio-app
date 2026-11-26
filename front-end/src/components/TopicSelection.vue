
<script setup>
import { decks } from '../data/decks'

const emit = defineEmits(['selectDeck', 'goHome'])

function selectDeck(deck) {
  emit('selectDeck', deck)
}
</script>

<template>
  <div class="page">
    <div class="header">
      <button class="back-button" @click="emit('goHome')">
        ← Dashboard
      </button>

      <h1>Choose a Deck</h1>
      <p>Select a topic to begin your study session.</p>
    </div>

    <div class="deck-list">
      <div
        v-for="deck in decks"
        :key="deck.id"
        class="deck-card"
      >
        <div>
          <h2>{{ deck.name }}</h2>
          <p>{{ deck.description }}</p>

          <span v-if="deck.available">
            {{ deck.cards.length }} flashcards
          </span>

          <span v-else>
            Coming soon
          </span>
        </div>

        <button
          :disabled="!deck.available"
          @click="selectDeck(deck)"
        >
          {{ deck.available ? 'Start Session →' : 'Coming Soon' }}
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.page {
  min-height: 100vh;
  background: #edf7f0;
  padding: 50px 20px;
}

.header {
  max-width: 750px;
  margin: 0 auto 35px;
}

.header h1 {
  color: #166534;
  font-size: 2.3rem;
  margin: 25px 0 10px;
}

.header p {
  color: #6b7280;
}

.back-button {
  background: transparent;
  border: none;
  color: #166534;
  cursor: pointer;
  font-size: 1rem;
}

.deck-list {
  max-width: 750px;
  margin: auto;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.deck-card {
  background: white;
  padding: 25px;
  border: 1px solid #dcfce7;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
}

.deck-card h2 {
  color: #166534;
  margin-bottom: 8px;
}

.deck-card p {
  color: #6b7280;
  margin-bottom: 12px;
}

.deck-card span {
  font-size: 0.85rem;
  color: #16a34a;
}

.deck-card button {
  padding: 12px 18px;
  border: none;
  border-radius: 9px;
  background: #22c55e;
  color: white;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
}

.deck-card button:disabled {
  background: #d1d5db;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .deck-card {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
