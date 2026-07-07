const API_URL = 'http://127.0.0.1:5000'

export async function registerUser(email, password) {
   const response = await fetch(`${API_URL}/register`, {
      method: 'POST',
      headers: {
         'Content-Type': 'application/json'
      },
      body: JSON.stringify({
         email,
         password
      })
   })
   const data = await response.json()
   console.log(data)
}