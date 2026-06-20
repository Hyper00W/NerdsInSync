# GrindSync 🚀

> Two people. One goal. Consistency over motivation.

---

## The Problem

Most productivity apps measure time.

Most coding platforms measure submissions.

Neither answers the question that actually matters:

**Who genuinely showed up and put in the work today?**

GrindSync is an attempt to solve that.

Not by counting hours.
Not by counting solved problems.

But by building a system that makes consistent effort visible.

---

## What is GrindSync?

GrindSync is a backend-first platform designed to help two people stay accountable while learning.

Whether it's:

* DSA
* Backend Development
* System Design
* Machine Learning
* Interview Preparation

the goal is simple:

Track progress, compare consistency, and create an environment where effort matters.

---

## Current Progress

### Backend Foundation ✅

* FastAPI setup
* PostgreSQL integration
* SQLAlchemy ORM configuration
* Environment variable management
* Database connectivity established
* Database dependency injection using FastAPI

### User Management ✅

* User model created
* Users table generated
* Request validation using Pydantic
* User registration endpoint implemented
* User data persistence to PostgreSQL

### Authentication System 🚧

* Password hashing with bcrypt
* Password verification
* Login endpoint implemented
* User lookup using SQLAlchemy queries
* Authentication flow completed

### Development Status

```text
Foundation         ██████████ 100%
Authentication     ████████░░ 80%
Core Features      ░░░░░░░░░░ 0%
Real-Time Layer    ░░░░░░░░░░ 0%
Automation Layer   ░░░░░░░░░░ 0%
```

---

## Current Architecture

```text
Client
   │
   ▼
FastAPI Routes
   │
   ▼
Pydantic Schemas
   │
   ▼
SQLAlchemy ORM
   │
   ▼
PostgreSQL
```

### Authentication Flow

```text
Register
   │
   ▼
Validate Request
   │
   ▼
Hash Password
   │
   ▼
Store User

Login
   │
   ▼
Find User By Email
   │
   ▼
Verify Password
   │
   ▼
Success / Failure
```

---

## Tech Stack

### Backend

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Passlib (bcrypt)

### Tools

* Git
* GitHub
* dotenv

---

## Why This Project?

As a Computer Science student preparing for placements, I spend a significant amount of time solving problems, learning new technologies, and trying to stay consistent.

One thing I noticed:

* Streaks can be manipulated.
* Problem counts can be misleading.
* Logged hours don't always represent actual effort.

This project started as a question:

**Can accountability be designed better?**

GrindSync is my attempt to explore that idea while learning backend development from the ground up.

---

## Roadmap

### Phase 1 — Foundation

* [x] FastAPI Setup
* [x] PostgreSQL Setup
* [x] SQLAlchemy Configuration
* [x] User Model
* [x] User Schema
* [x] Registration Endpoint

### Phase 2 — Authentication

* [x] Password Hashing
* [x] Password Verification
* [x] Login Endpoint
* [ ] JWT Authentication
* [ ] Protected Routes

### Phase 3 — Social Layer

* [ ] Friend Requests
* [ ] Friend Management
* [ ] User Connections

### Phase 4 — Accountability System

* [ ] Study Sessions
* [ ] Session Tracking
* [ ] Activity Metrics
* [ ] Daily Score System
* [ ] Leaderboards

### Phase 5 — Real-Time Experience

* [ ] WebSockets
* [ ] Live Activity Updates
* [ ] Online Presence

### Phase 6 — The Interesting Part 👀

A few ideas are intentionally missing from this README.

The long-term vision involves reducing manual tracking and exploring more objective ways to measure consistency and effort.

---

## What I'm Learning

This project is helping me gain practical experience with:

* Backend Architecture
* REST APIs
* Database Design
* SQLAlchemy ORM
* Authentication & Security
* API Design
* Dependency Injection
* Scalable Project Structure

---

## Project Status

Actively under development.

Built step by step while learning backend engineering in public.

Every feature in this repository is being implemented from scratch to understand not only how it works, but why it works.

### Current Milestone

✅ User Registration

✅ Password Hashing

✅ Login Authentication

🔜 JWT Authentication

⭐ Follow the project if you'd like to see where it goes.
