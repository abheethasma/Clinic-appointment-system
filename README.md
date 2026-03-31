<div align="center">

<br/>

```
 ██████╗██╗     ██╗███╗   ██╗██╗ ██████╗
██╔════╝██║     ██║████╗  ██║██║██╔════╝
██║     ██║     ██║██╔██╗ ██║██║██║
██║     ██║     ██║██║╚██╗██║██║██║
╚██████╗███████╗██║██║ ╚████║██║╚██████╗
 ╚═════╝╚══════╝╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝
```

# 🏥 Clinic Appointment System

### A Microservices Architecture built with FastAPI

<br/>

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)](https://www.uvicorn.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![License](https://img.shields.io/badge/License-Academic-blueviolet?style=for-the-badge)](LICENSE)

<br/>

> **An academic microservices project** demonstrating how real-world clinic operations can be decomposed into independent, scalable services connected via a centralized API Gateway.

<br/>

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Architecture](#-architecture)
- [Microservices](#-microservices)
- [Technologies](#-technologies)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Running the Services](#-running-the-services)
- [API Documentation](#-api-documentation)
- [Testing](#-testing)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 🧭 Overview

The **Clinic Appointment System** is a backend application that models the core operations of a medical clinic. Rather than building a traditional monolith, this project applies **microservices architecture** — splitting the system into independent services, each responsible for a specific domain.

All services are connected through a single **API Gateway**, giving clients one clean entry point to the entire system.

---

## 🏗️ Architecture

```
                          ┌─────────────────────────────┐
                          │         CLIENT / UI          │
                          └──────────────┬──────────────┘
                                         │
                                         ▼
                          ┌─────────────────────────────┐
                          │        API GATEWAY           │
                          │         Port: 8000           │
                          └──┬──────┬──────┬──────┬─────┘
                             │      │      │      │
               ┌─────────────┘  ┌───┘  ┌──┘  └────────────┐
               ▼                ▼      ▼                    ▼
      ┌──────────────┐  ┌──────────┐  ┌────────────┐  ┌───────────────┐
      │   Patient    │  │  Doctor  │  │Appointment │  │   Feedback    │
      │   Service   │  │  Service │  │  Service  │  │    Service    │
      │  Port: 8001  │  │Port:8002 │  │ Port:8003 │  │  Port: 8004  │
      └──────────────┘  └──────────┘  └────────────┘  └───────────────┘
```

The **API Gateway** is the single entry point — clients never communicate directly with individual services. This keeps the system clean, manageable, and easy to extend.

---

## 🔧 Microservices

| Service | Port | Responsibility |
|---|---|---|
| 🌐 **API Gateway** | `8000` | Routes requests to the appropriate microservice |
| 🧑‍⚕️ **Patient Service** | `8001` | Manage patient records and details |
| 👨‍⚕️ **Doctor Service** | `8002` | Manage doctor profiles and availability |
| 📅 **Appointment Service** | `8003` | Book, update, and manage appointments |
| 💬 **Feedback Service** | `8004` | Collect and manage patient feedback |

---

## 💻 Technologies

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **FastAPI** | High-performance web framework for building APIs |
| **Uvicorn** | Lightning-fast ASGI server |
| **Pydantic** | Data validation and schema modeling |
| **HTTPX** | Async HTTP client for inter-service communication |

---

## 📁 Project Structure

```
clinic-appointment-system/
│
├── gateway/
│   └── main.py                  ← API Gateway — single entry point
│
├── patient-service/
│   ├── models.py                ← Data models
│   ├── data_service.py          ← In-memory data layer
│   ├── service.py               ← Business logic
│   └── main.py                  ← FastAPI app & routes
│
├── doctor-service/
│   ├── models.py
│   ├── data_service.py
│   ├── service.py
│   └── main.py
│
├── appointment-service/
│   ├── models.py
│   ├── data_service.py
│   ├── service.py
│   └── main.py
│
├── feedback-service/
│   ├── models.py
│   ├── data_service.py
│   ├── service.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Services

Open **5 separate terminal windows** and run each service:

```bash
# Terminal 1 — Patient Service
cd patient-service
python -m uvicorn main:app --reload --port 8001

# Terminal 2 — Doctor Service
cd doctor-service
python -m uvicorn main:app --reload --port 8002

# Terminal 3 — Appointment Service
cd appointment-service
python -m uvicorn main:app --reload --port 8003

# Terminal 4 — Feedback Service
cd feedback-service
python -m uvicorn main:app --reload --port 8004

# Terminal 5 — API Gateway (start last)
cd gateway
python -m uvicorn main:app --reload --port 8000
```

> ⚠️ **Start the API Gateway last**, after all other services are running.

---

## 📖 API Documentation

FastAPI automatically generates interactive Swagger UI documentation for each service.

| Service | Swagger URL |
|---|---|
| 🌐 API Gateway | http://localhost:8000/docs |
| 🧑‍⚕️ Patient Service | http://localhost:8001/docs |
| 👨‍⚕️ Doctor Service | http://localhost:8002/docs |
| 📅 Appointment Service | http://localhost:8003/docs |
| 💬 Feedback Service | http://localhost:8004/docs |

### Example Gateway Endpoints

```
GET    /gateway/patients          ← List all patients
GET    /gateway/doctors           ← List all doctors
GET    /gateway/appointments      ← List all appointments
GET    /gateway/feedbacks         ← List all feedback entries
```

> All CRUD operations (Create, Read, Update, Delete) are available through the gateway for each resource.

---

## 🧪 Testing

The project was tested using:

- ✅ **FastAPI Swagger UI** — interactive endpoint testing
- ✅ **Direct service endpoints** — individual microservice verification
- ✅ **API Gateway endpoints** — end-to-end gateway routing

All CRUD operations were successfully verified across all four microservices.

---

## 🛣️ Future Improvements

- [ ] 🗄️ **Database integration** — replace in-memory storage with PostgreSQL or MongoDB
- [ ] 🔐 **Authentication & Authorization** — JWT-based access control
- [ ] 📊 **Logging & Monitoring** — centralized logging with tools like Prometheus / Grafana
- [ ] 🔍 **Service Discovery** — dynamic service registration
- [ ] 🐳 **Docker & Kubernetes** — containerized deployment with orchestration

---

> This project was developed as part of an academic assignment to demonstrate microservices architecture principles using FastAPI.

---

<div align="center">

**⭐ If this project helped you, consider giving it a star!**

*This project is for academic and learning purposes.*

</div>
