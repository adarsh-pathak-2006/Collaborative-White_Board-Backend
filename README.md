# 🎨 Collaborative Whiteboard API

A robust, real-time backend for the Collaborative Whiteboard application, built with **Django**, **Django REST Framework**, and **Django Channels**.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white)

## ✨ Features

- **JWT Authentication**: Secure login and registration using `rest_framework_simplejwt`.
- **Real-Time Collaboration**: High-performance WebSocket endpoints powered by Django Channels and Redis to sync drawing states across clients instantly.
- **Room Management**: Create, join, and manage whiteboard rooms seamlessly through RESTful APIs.
- **Asynchronous Task Logging**: Celery integration for non-blocking database writes to track all drawing actions.

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Redis Server (Required for Channels and Celery)

### Installation

1. **Clone the repository and navigate to the backend:**
   ```bash
   cd whiteboard
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   # (Ensure you also install packages like daphne, channels-redis, celery, django-cors-headers, and python-dotenv)
   ```

3. **Environment Setup:**
   Copy the example environment file and configure your secrets:
   ```bash
   cp .env.example .env
   ```
   *Note: Never commit your `.env` file to version control.*

4. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Services:**

   - **Django Server (ASGI):**
     ```bash
     python manage.py runserver
     ```
   
   - **Celery Worker:**
     ```bash
     celery -A whiteboard worker -l info
     ```
   
   - **Redis Server:** Ensure your local Redis instance is running on `127.0.0.1:6379`.

## 📡 API Endpoints

### Authentication
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Obtain JWT access and refresh tokens
- `POST /api/auth/token/refresh/` - Refresh JWT token
- `GET /api/auth/my-profile/` - Get current user profile

### Rooms
- `GET/POST /api/board/rooms/` - List or create rooms
- `GET /api/board/rooms/<id>/` - Retrieve specific room details
- `POST /api/board/room-members/<id>/` - Join a room

### WebSockets
- `ws://<host>/ws/room/<id>/?token=<jwt_token>` - Connect to a specific whiteboard room for real-time syncing.

## 🛠️ Architecture

- **Django Channels** handles the WebSocket connections, leveraging a custom JWT Authentication middleware to authorize clients via query parameters.
- **Redis Channel Layer** broadcasts drawing events (coordinates, color, brush size) across all users in the same room group.
- **Celery** is used to offload `DrawLog` creations to background tasks, keeping the WebSocket loop highly responsive.

---
*Built with ❤️ for real-time collaboration.*
