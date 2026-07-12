<script setup>
import SignupForm from './SignupForm.vue'
import LogInForm from './LogInForm.vue'
import { ref } from 'vue'
const showLogin = ref(false)
const emit = defineEmits(['loginSuccess'])
</script>

<template>
    <div class="auth-page">
        <h1>IB Biology Flashcards</h1>
        <h3>Welcome! Create an account to get started. Or log in!</h3>
        <SignupForm
        v-if="!showLogin"
        @switchToLogin="showLogin = true"
        @loginSuccess="emit('loginSuccess')"
        />
        <LogInForm
        v-else
        @switchToSignup="showLogin = false"
        @loginSuccess="emit('loginSuccess')"
        />
    </div>
</template>

<style scoped>

.auth-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    padding: 20px;
}
</style>