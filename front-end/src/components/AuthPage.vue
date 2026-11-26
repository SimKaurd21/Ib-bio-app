<script setup>
import SignupForm from './SignupForm.vue'
import LogInForm from './LogInForm.vue'
import { ref } from 'vue'
const showLogin = ref(false)
const userId = ref(null)
const emit = defineEmits(['loginSuccess'])
const isLoading = ref(false)

function handleAuthLoading(value) {
    isLoading.value = value
}

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
        @authLoading="handleAuthLoading"
        />
        <LogInForm
            v-else
            @switchToSignup="showLogin = false"
            @loginSuccess="handleLoginSuccess"
            @authLoading="handleAuthLoading"
        />
        <div v-if="isLoading" class="loading-overlay">
            <div class="spinner"></div>
                <p>Preparing your BioRecall experience...</p>
        </div>
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

.auth-page {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    padding: 20px;
}

.loading-overlay {
    position: fixed;
    inset: 0;
    background: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.spinner {
    width: 45px;
    height: 45px;
    border: 4px solid #e5e7eb;
    border-top-color: #26976b;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
}

@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}
</style>