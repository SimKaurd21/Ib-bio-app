# Biorecall
This is a fullstack application that helps IB Biology students with the
enzymes and metabolism topic of the IB Biology curriculum through flashcards.
The format helps students utilize active recall.

<img width="1016" height="667" alt="signUp" 
src="https://github.com/user-attachments/assets/6dd35ab6-883b-491d-957d-5a8ab5297a70" />


<img width="714" height="599" alt="flashcard" 
src="https://github.com/user-attachments/assets/d99fd75b-8198-424c-b4eb-cf31a3d82ba1" />

## Features

- User authentication (register/login)
- Interactive flashcard sessions
- Mark cards for review
- Personalized review sessions
- Save personal notes
- Saves user progress

## Tech Stack

### Frontend
- Vue.js
- Vite
- JavaScript
- CSS

### Backend
- Flask
- Python

### Database
- PostgreSQL (Neon)

### Other
- REST API
- Git
- GitHub
- Vercel
- Render

## Live Demo
https://biorecall.vercel.app/

## Why I built this
I'm a first year computer science student who wanted to learn skills while
providing ib biology students with a place to house the notes they took from the 
biologyforlife website. I got permission from the owner of the website to utilize
the bullet point syllabus structure in my flashcard application. I love mixing technology
and education while learning new things at the same time!

## Challenges

Some of the challenges I solved included:

- Designing a REST API between Vue and Flask
- Switching databases from sqlite to PostgreSQL
- Persisting user progress using PostgreSQL
- Loading saved user data after login
- Preventing users from reviewing marked cards if they
didn't mark any cards for review

## What I Learned

This project taught me how to:

- Build a complete full-stack application
- Design REST APIs
- Connect a frontend to a backend
- Work with SQL databases
- Implement user authentication
- Deploy web applications

## Future Improvements

- Spaced repetition algorithm
- Search flashcards
- Multiple IB Biology topics
- Mobile optimization
- Saving user position when they leave a session

## Content Attribution

Flashcard bullet points are adapted from Biology for Life and are used with permission from the creator.
Answer explanations are intended as refreshers and are not enough to score well on the ib exams.
Users are encouraged to use biologyforlife 
alongside this application for comprehensive IB Biology study.
See ATTRIBUTION.md for additional information.

## Installation

Clone the repository
git clone ...
Install frontend dependencies
npm install
Install backend dependencies
pip install -r requirements.txt
Run the Flask server
Run the Vue development server
