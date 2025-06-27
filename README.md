# 🔐 Secure Incident Reporting System (FastAPI + PostgreSQL)

A secure, role-based API backend for reporting and tracking security incidents. Built with FastAPI, PostgreSQL, and JWT authentication. Designed to simulate scalable deployment on AWS Lambda using Zappa-compatible architecture.

---

## 🚀 Features

- ✅ **User Registration & Login** (JWT-based auth)
- ✅ **Role-Based Access Control** (admin-only routes)
- ✅ **Incident Reporting** (create, filter, delete)
- ✅ **Filtering by severity & status** via query params
- ✅ **Admin-only deletion of incidents**
- ✅ **JWT Token Auth** (via Swagger Authorize)
- ✅ **Dockerized** (PostgreSQL + FastAPI stack)
- ✅ **AWS Lambda compatible** (via `Mangum`)
- ✅ **CI with GitHub Actions** + `.env` secret injection
- ✅ **Custom OpenAPI schema** (for proper Swagger UI behavior)

---

## 🛠️ Tech Stack

| Layer          | Technology                     |
|----------------|--------------------------------|
| Language       | Python 3.11 / 3.12              |
| Framework      | FastAPI                        |
| Database       | PostgreSQL                     |
| Auth           | JWT via `python-jose`, bcrypt  |
| ORM            | SQLAlchemy                     |
| Containerization| Docker + Docker Compose       |
| AWS Simulation | `Mangum` (for Lambda deploy)   |
| CI/CD          | GitHub Actions                 |

---

## 📂 Project Structure

```
secure-incident-reporting/
├── app/
│   ├── api/               # Routers (auth, incidents)
│   ├── core/              # Configs, security
│   ├── db/                # Models, database session
│   └── main.py            # FastAPI app entrypoint
├── tests/                 # (Optional) Pytest test cases
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

## 🐳 Running Locally (with Docker)

```bash
# Build and start containers
docker-compose up --build

# Visit the API docs at:
# 👉 http://localhost:8000/docs (Swagger)
# 👉 http://localhost:8000/redoc (ReDoc)
```

---

## 🔐 API Authentication

This API uses **JWT Bearer tokens** for secure access.

### Auth Flow:
1. **Register** a user → `POST /auth/register`
2. **Login** → `POST /auth/login`  
   → Receive `access_token` in response.
3. Use the token in Swagger UI via **"Authorize"** →  
   `Bearer <your_token_here>`

---

## 📬 API Documentation

| UI       | URL                         | Description                          |
|----------|-----------------------------|--------------------------------------|
| Swagger  | `http://localhost:8000/docs`  | Interactive docs with JWT testing    |
| ReDoc    | `http://localhost:8000/redoc` | Read-only clean API documentation    |
| Root     | `http://localhost:8000/`      | Welcome message                      |


---

## 🧩 Simulated AWS Lambda Integration

This project integrates `Mangum` to simulate AWS Lambda deployment locally. This makes it compatible with:

- **Zappa** or **AWS API Gateway + Lambda**
- **Serverless architecture** best practices
- **CI-ready** with secrets managed via GitHub Actions

> While no actual AWS services are used, the backend is **architecturally ready** for cloud-native deployment.

---

## 📦 Requirements

Install Python packages (if running without Docker):

```bash
pip install -r requirements.txt
```

---

## ✨ Made with FastAPI, PostgreSQL, Docker — Simulating Scalable Secure Systems

_made by arjun7579_