<script setup>
    import {ref} from 'vue'
    import { loginUser } from '../services/api' 
    const email = ref('')
    const password = ref('')
    const message = ref('')
    const emit = defineEmits(['switchToSignup'], ['loginSuccess'])

async function handleLogin() {
   try {
      const result = await loginUser(email.value, password.value)
      emit('loginSuccess')

      message.value = result.message
      emit('loginSuccess')
   } catch (error) {
      message.value = error.message
   }
}
</script>

<template>
    <div class="login-form">
        <h2>Log In</h2>

        <input
        v-model="email"
        placeholder="Email"
        />

        <input
        v-model="password"
        type="password"
        placeholder="Password"
        />

        <button @click="handleLogin">
            Log In
        </button>

        <p>{{ message }}</p>

        <button @click="emit('switchToSignup')">
            Don't have an account? Sign up!
        </button>
    </div>
</template>