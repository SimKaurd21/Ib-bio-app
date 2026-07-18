const API_URL = 'https://biology-flashcard-biorecall.onrender.com/'

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
   
   if (!response.ok) {
      throw new Error(data.message)
   }

   return data
}

export async function loginUser(email, password) {
   const response = await fetch(`${API_URL}/login`, {
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

   if (!response.ok) {
      throw new Error(data.message)
   }

   return data
}

export async function saveReview(userId, cardId) {
   const response = await fetch(`${API_URL}/review`, {
      method: 'POST',
      headers: {
         'Content-Type': 'application/json'
      },
      body: JSON.stringify({
         user_id: userId,
         card_id: cardId
      })
   })
   const data = await response.json()

   if (!response.ok) {
      throw new Error(data.message)
   }
   return data
}

export async function getReviewCards(userId) {
   const response = await fetch(`${API_URL}/review/${userId}`)

   const data = await response.json()

   if (!response.ok) {
      throw new Error(data.message)
   }

   return data
}

export async function deleteReviewCard(userId, cardId) {
   const response = await fetch(
      `${API_URL}/review/${userId}/${cardId}`,
      {
         method: "DELETE"
      }
   )

   const data = await response.json()

   if (!response.ok) {
      throw new Error(data.message)
   }

   return data
}

export async function saveUserAnswer(userId, cardId, answerText) {
   const response = await fetch(`${API_URL}/user_answers`, {
      method: 'POST',
      headers: {
         'Content-Type': 'application/json'
      },
      body: JSON.stringify({
         user_id: userId,
         card_id: cardId,
         answer: answerText
      })
   })

   const data = await response.json()

   if (!response.ok) {
      throw new Error(data.message)
   }

   return data
}

export async function getUserAnswers(userId, cardId) {
   const response = await fetch(`${API_URL}/user_answers/${userId}/${cardId}`)
   
   const data = await response.json()
   if (!response.ok) {
      throw new Error(data.message)
   }

   return data
}