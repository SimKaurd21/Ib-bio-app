<script setup>
import SignupForm from './SignupForm.vue'
import LogInForm from './LogInForm.vue'
import { ref } from 'vue'
const showLogin = ref(false)
const userId = ref(null)
const emit = defineEmits(['loginSuccess'])

function handleLoginSuccess(id) {
    userId.value = id
    emit('loginSuccess', id)
}
</script>

<template>
    <div class="auth-page">
        <SignupForm
        v-if="!showLogin"
        @switchToLogin="showLogin = true"
        @loginSuccess="handleLoginSuccess"
        />
        <LogInForm
            v-else
            @switchToSignup="showLogin = false"
            @loginSuccess="handleLoginSuccess"
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