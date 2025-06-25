# 🧵 Social Media API – Django REST Framework

This project allows users to create posts, like, share, retweet, comment, and reply to comments. Ideal for learning API design, nested relationships, and REST principles in Django.

---

## 📌 Features

- 🔐 User Registration
- 📝 Create text-based Posts
- ❤️ Like a Post (only once per user)
- 🔁 Share a Post (multiple times allowed)
- 💬 Comment on Posts (with nested replies)
- 🔄 Retweet/Quote with custom text
- 📊 View Post Details with full stats

---

## 🚀 Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite (default DB, replaceable with PostgreSQL)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone git@github.com:your-username/social-media-api.git
cd social-media-api
python3 -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
ppython manage.py runserver
python manage.py migrate

