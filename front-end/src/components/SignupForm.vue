<script setup>
import { ref } from 'vue'
import { registerUser } from '../services/api'
const email = ref('')
const password = ref('')

async function handleRegister() {
   const data = await registerUser(
      email.value,
      password.value
   )

   console.log(data)
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
    </div>
</template>