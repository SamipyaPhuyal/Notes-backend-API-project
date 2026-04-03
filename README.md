# Streaming Site API

A RESTful API built with Django REST Framework (DRF) for a Notes Sharing Platform  that allows users to view, share, and like,bookmark Notes. Demonstrates authentication, authorization, pagination, filtering, throttling, and JWT API access.

## Features
- User registration, login, and logout
- JWT authentication 
- CRUD operations for Notes
- Pagination for large datasets
- Filtering
- throttling
- Browsable API interface for easy testing
- permissions

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Authentication:** JWT Authentication
- **Database:** SQLite (default), compatible with PostgreSQL/MySQL
- **Filters & Pagination:** DjangoFilterBackend, PageNumberPagination
- **Testing & API Exploration:** Postman / DRF Browsable API / Swagger

## Setup Instructions
```bash
--git clone <repository-url>
--cd StreamingSite-DRF-Project
--python -m venv venv
--venv\Scripts\activate  # Windows
--pip install -r requirements.txt
--python manage.py migrate
--python manage.py createsuperuser  # Optional
--python manage.py runserver

```markdown
##📌 API Endpoints
🧭 Dashboard
GET /dashboard/ → Get dashboard data
📝 Notes
📄 Notes List & Create
GET /notes/list/ → List all notes
POST /notes/list/ → Create a new note
🔍 Note Detail (CRUD)
GET /notes/detail/{id}/ → Retrieve a note
PUT /notes/detail/{id}/ → Update note (full)
PATCH /notes/detail/{id}/ → Update note (partial)
DELETE /notes/detail/{id}/ → Delete note
🔖 Bookmark
POST /notes/detail/{id}/bookmark/ → Add bookmark
DELETE /notes/detail/{id}/bookmark/ → Remove bookmark
❤️ Like
POST /notes/detail/{id}/like/ → Like a note
DELETE /notes/detail/{id}/like/ → Unlike a note
👤 Users
📋 User List
GET /users/list/ → List users
🔐 Authentication
POST /users/register/ → Register new user
POST /users/login/ → Login user
POST /users/logout/ → Logout user
POST /users/refresh-token/ → Refresh authentication token
👤 Profile
GET /users/profile/ → Get current user profile
