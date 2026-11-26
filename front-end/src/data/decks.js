import { cards } from './cards'
import {dnaReplicationCards} from './dna-replication.js'

export const decks = [
  {
    id: 'enzymes-and-metabolism',
    name: 'Enzymes and Metabolism',
    description: 'Practice Enzymes and Metabolism Topic C1.1',
    cards: cards,
    available: true
  },

  {
    id: 'dna-replication',
    name: 'DNA Replication',
    description: 'Practice DNA replication Topic D1.1',
    cards: dnaReplicationCards,
    available: true
  }
]

export const allCards = decks.flatMap(deck => deck.cards)