# 📰 Django Blog Site

A simple fully responsive blog platform built with Django, where multiple users can create, edit, and manage their own blog posts. Each blog can include an image, and all posts are visible to all users. It also includes a basic user authentication system — users can sign up, log in, and see all blogs or just the ones they've written.

---

## 🔧 What You Can Do

- Register and log in as a user
- Create blog posts with or without images
- Edit or delete your own posts
- View all blogs from all users
- View only your own blogs from your profile/dashboard

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (default)
- **Frontend:** HTML, CSS (Bootstrap optional)
- **Auth:** Django’s built-in authentication

---


## 🚀 Getting Started

```bash
git clone https://github.com/I-Am-Anurag-Rawat/BlogHub-By-Django.git
cd BlogHub-By-Django
python -m venv .venv
.venv\Scripts\activate # or on mac ->  source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver