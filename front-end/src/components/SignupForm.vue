<script setup>
import { ref } from 'vue'
import { registerUser } from '../services/api'
const email = ref('')
const password = ref('')
const message = ref('')
const emit = defineEmits(['switchToLogin'], ['loginSuccess'])

async function handleRegister() {
    try { 
        const data = await registerUser(
        email.value,
        password.value
        )
        console.log(data)
        message.value = data.message
        emit('loginSuccess')
    } catch (error) {
        message.value = error.message
    }
    
}

</script>

<template>
    <div>
        <h2>Create Account</h2>

        <input
        v-model="email"
        placeholder="Email"
        />

        <input
        v-model="password"
        type="password"
        placeholder="Password"
        />

        <button @click="handleRegister">
            Create Account
        </button>
        <p>{{ message }}</p>

        <button @click="emit('switchToLogin')">
            Already have an account? Log in!
        </button>
    </div>
</template>

<style scoped>
    div {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 150vh;
        padding: 20px;
        background-color: #d7d7d784;
        border-radius: 25px;
    }

    input {
        margin-bottom: 10px;
        padding: 10px;
        width: 200px;
    }

    button {
        padding: 10px, 20px;
        background-color: #4CAF50;
        color: white;
        border: none;
        cursor: pointer;
    }

    button:hover {
        background-color: #724403;
    }
</style>