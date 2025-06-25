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
- SQLite (default DB)

---
## 🧪 API Endpoints
| Action             | Method | Endpoint           | Body Parameters                                               |
| ------------------ | ------ | ------------------ | ------------------------------------------------------------- |
| Register User      | POST   | `/api/users/`      | `username`, `password`                                        |
| Create Post        | POST   | `/api/posts/`      | `user`, `text`, `original_post?`                              |
| Like a Post        | POST   | `/api/likes/`      | `user`, `post`                                                |
| Share a Post       | POST   | `/api/shares/`     | `user`, `post`                                                |
| Retweet a Post     | POST   | `/api/retweets/`   | `user`, `text`, `original_post`                               |
| Comment on Post    | POST   | `/api/comments/`   | `user`, `post`, `text`, `parent?`                             |
| Grade a Post (1-5) | POST   | `/api/grades/`     | `user`, `post`, `score (1-5)`                                 |
| Get Post Details   | GET    | `/api/posts/<id>/` | Returns likes, shares, retweets, comments, replies, avg grade |

## ⚙️ Setup Instructions


```bash
git clone git@github.com:your-username/social-media-api.git
cd social-media-api
python3 -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

