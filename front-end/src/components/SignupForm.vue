<script setup>
import { ref } from 'vue'
import { registerUser } from '../services/api'
const email = ref('')
const password = ref('')
const message = ref('')
const loading = ref(false)
const emit = defineEmits(['switchToLogin'], ['loginSuccess'])

async function handleRegister() {
  loading.value = true
  try {
    const data = await registerUser(
      email.value,
      password.value
    )
    localStorage.setItem(
      "userId",
      data.user_id
    )

    emit("loginSuccess", data.user_id)
  } catch(error) {
    message.value = error.message

  } finally {
    loading.value = false
  }
}

</script>

<template>
  <div class="signup-page">
    <div class="signup-card">

      <h1>🌿 BioRecall</h1>
      <p class="subtitle">
        Master IB Biology using active recall.
      </p>

      <div class="input-group">
        <label>Email</label>
        <input
          v-model="email"
          type="email"
          placeholder="Enter your email"
        />
      </div>

      <div class="input-group">
        <label>Password</label>
        <input
          v-model="password"
          type="password"
          placeholder="Create a password"
        />
      </div>

      <button
        class="primary-button"
        @click="handleRegister"
        :disabled="loading"
      >
        {{ loading ? "Creating account..." : "Sign Up" }}
      </button>

      <p class="message">
        {{ message }}
      </p>

      <button
        class="text-button"
        @click="emit('switchToLogin')"
      >
        Already have an account?
      </button>
    </div>
  </div>
</template>

<style scoped>
    .signup-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #edf7f0;
  padding: 20px;
}

.signup-card {
  width: 400px;
  background: white;
  border-radius: 20px;
  padding: 40px;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
}

h1 {
  text-align: center;
  color: #166534;
  margin-bottom: 10px;
}

.subtitle {
  text-align: center;
  color: #6b7280;
  margin-bottom: 35px;
  line-height: 1.5;
}

.input-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

label {
  margin-bottom: 8px;
  font-weight: 600;
  color: #374151;
}

input {
  padding: 14px;
  border-radius: 12px;
  border: 2px solid #d1d5db;
  font-size: 15px;
  transition: 0.2s;
}

input:focus {
  outline: none;
  border-color: #22c55e;
  box-shadow: 0 0 0 4px rgba(34, 197, 94, 0.15);
}

.primary-button {
  width: 100%;
  margin-top: 10px;
  padding: 14px;
  border: none;
  border-radius: 12px;
  background: #22c55e;
  color: white;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.primary-button:hover {
  background: #16a34a;
  transform: translateY(-2px);
}

.text-button {
  width: 100%;
  margin-top: 20px;
  background: none;
  border: none;
  color: #166534;
  cursor: pointer;
  font-weight: 600;
}

.text-button:hover {
  text-decoration: underline;
}

.message {
  text-align: center;
  color: #16a34a;
  min-height: 22px;
  margin-top: 15px;
}
</style>