 (Pinterest Clone API) 

A production-ready REST API backend clone of Pinterest, built with Django and Django REST Framework. This project was developed as a **Diploma Degree Final Project** to demonstrate full-stack backend architecture, algorithm design for content feeds, and cloud deployment on Vercel.

---

## 📸 Features

- **JWT Authentication**: Secure signup, login, and profile management.
- **Pin Creation**: Upload images (stored on Cloudinary CDN) with titles and descriptions.
- **Boards**: Organize pins into customizable public/private boards.
- **Social Graph**: Follow/unfollow users.
- **Smart Home Feed Algorithm**: Not just chronological order. A custom **Weighted Scoring Algorithm** calculates feed ranking based on:
  - **Recency Decay** (time-based relevance)
  - **Engagement Score** (views + saves)
- **Admin Dashboard**: Django's built-in admin interface for content moderation.
- **Serverless Ready**: Configured for deployment on **Vercel** with PostgreSQL and serverless functions.

---

## 🧠 The Feed Algorithm Explained

The core of this project is the `HomeFeedView` algorithm. Unlike basic "latest posts" feeds, this implementation uses a hybrid scoring model:
