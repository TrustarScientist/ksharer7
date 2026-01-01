# KSHARER 🚀  
A community-driven knowledge-sharing platform with built-in monetization.

---

## 🧠 Overview

**KSHARER** is a modern knowledge-sharing platform designed to make learning accessible, practical, and community-driven.  
It combines social interaction, structured knowledge communities (called *Niches*), and a built-in digital wallet to enable creators to share and monetize high-quality educational content.

KSHARER sits at the intersection of:
- Social media
- E-learning
- Creator economy

---

## 🎯 Problem Statement

Learning resources today are:
- Scattered across multiple platforms
- Expensive or inaccessible
- Poorly structured
- Lacking incentives for knowledgeable people to teach

KSHARER solves this by providing a single ecosystem where:
- Knowledge is organized into communities (*Niches*)
- Creators can monetize resources (ebooks, guides, files)
- Learners can interact, ask questions, and grow together

---

## ✨ Core Features (MVP)

### 🏷 Niches
Community spaces for knowledge sharing.
- Predefined public Niches (e.g. Education, Technology)
- Each post and resource belongs to a Niche

### 💬 Thoughts
Short, social posts shared within Niches.
- Similar to micro-blogging
- Encourages discussion and idea sharing

### 📚 Resources
Monetizable educational content.
- Ebooks, PDFs, files
- Free or paid using virtual coins
- Secure access after purchase

### 💰 Wallet & ZiniCoin
Built-in virtual wallet system.
- Users fund wallets via Paystack
- Resources are purchased using **ZiniCoin**
- Designed to make paid learning frictionless

### ⚡ App-Like Experience (No SPA)
- Server-rendered Django templates
- **HTMX** for partial page updates
- **Alpine.js** for UI interactivity
- Minimal reloads, fast performance

---

## 🛠 Tech Stack

### Backend
- **Django**
- PostgreSQL
- Django Templates

### Frontend
- Tailwind CSS (CDN)
- HTMX
- Alpine.js

### Storage
- Cloudinary (user-uploaded files)
- Whitenoise (static files)

### Payments
- Paystack

### Hosting
- Render (Web Service, PostgreSQL, Cron Jobs)

---

## 🧩 Project Structure

```text
ksharer/
│
├── config/                 # Project settings
├── apps/                   # Domain apps
│   ├── accounts/
│   ├── niches/
│   ├── thoughts/
│   ├── resources/
│   ├── wallet/
│   └── core/
│
├── templates/
├── static/
├── manage.py
└── requirements.txt

🚀 Getting Started (Local Setup)
1️⃣ Clone the repository
git clone https://github.com/your-username/ksharer.git
cd ksharer

2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Environment variables

Create a .env file and add:

SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://...
CLOUDINARY_CLOUD_NAME=...
CLOUDINARY_API_KEY=...
CLOUDINARY_API_SECRET=...
PAYSTACK_SECRET_KEY=...

5️⃣ Run migrations
python manage.py migrate

6️⃣ Start development server
python manage.py runserver


Visit: http://127.0.0.1:8000

🔐 User Roles

Regular Users

Join Niches

Post Thoughts

Purchase Resources

Creators

Upload paid or free resources

Earn ZiniCoin

Admins

Manage Niches

Moderate content

Oversee transactions

🧭 Product Philosophy

Learning should be accessible, not overpriced

Knowledge grows faster in communities

Creators deserve fair monetization

Simplicity beats over-engineering (especially in MVPs)

🔮 Roadmap (Post-MVP)

Private Niches with access control

PostChain (linked learning posts)

Virtual labs & hands-on environments

Creator analytics dashboard

Mobile app (API-driven)

AI-assisted learning tools

🤝 Contributing

KSHARER is in active development.
Contributions, feedback, and ideas are welcome.

Please open an issue or submit a pull request.

📜 License

This project is currently under a proprietary / restricted license.
Details will be updated before public open-source release.

👤 Author

Built by TrustarScientist
Computer Teacher & Software Developer

KSHARER is not just a platform.
It’s an ecosystem for sharing, learning, and growing together.


