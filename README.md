# 🚀 Backend MongoDB Challenge Tracker API

A fully functional backend system built using **FastAPI + MongoDB (Motor)** that supports:

* User Authentication (JWT-based)
* Challenge creation & participation
* Progress tracking system

---

# 🛠️ Tech Stack

* **FastAPI** – Backend framework
* **MongoDB Atlas** – Database
* **Motor** – Async MongoDB driver
* **JWT (python-jose)** – Authentication
* **Passlib (bcrypt)** – Password hashing

---

# ⚙️ Setup Instructions

## 1. Clone the repo

```bash
git clone <your-repo-url>
cd Backend-MongoDB-Project
```

---

## 2. Create virtual environment

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create `.env` file

```env
MONGO_URL=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority
DB_NAME=challenge_db

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## 5. Run server

```bash
uvicorn app.main:app --reload
```

---

## 6. Open API Docs

👉 http://127.0.0.1:8000/docs

---

# 🔐 Authentication Flow (JWT)

1. User registers:

   ```
   POST /auth/register
   ```

2. User logs in:

   ```
   POST /auth/login
   ```

3. Server returns JWT token:

   ```json
   {
     "access_token": "...",
     "token_type": "bearer"
   }
   ```

4. For protected routes:

   * Click **Authorize** in Swagger UI
   * Paste token (WITHOUT extra "Bearer")

5. Token is sent via header:

   ```
   Authorization: Bearer <token>
   ```

---

# 📦 API Endpoints

### 🔑 Auth

* `POST /auth/register`
* `POST /auth/login`

### 🏆 Challenges

* `POST /challenges/` → Create challenge
* `GET /challenges/` → List challenges
* `POST /challenges/{challenge_id}/join` → Join challenge

### 📈 Progress

* `POST /progress/` → Update progress

---

# 🗃️ Data Model Overview

## 🧑 Users Collection

```json
{
  "_id": ObjectId,
  "email": "user@gmail.com",
  "password": "hashed_password",
  "created_at": datetime
}
```

---

## 🏆 Challenges Collection

```json
{
  "_id": ObjectId,
  "title": "Hackathon",
  "description": "...",
  "target_value": 7,
  "duration_days": 30,
  "is_active": true,
  "created_at": datetime
}
```

---

## 📊 User Challenges Collection

```json
{
  "_id": ObjectId,
  "user_id": "user_id_string",
  "challenge_id": "challenge_id_string",
  "joined_at": datetime,
  "progress": 0
}
```

---

# ⚠️ Common Mistakes Faced (Important Learning)

During development, several real-world issues were encountered:

### 1. ❌ JWT Misuse in Swagger

* Mistake: Added `"Bearer Bearer <token>"`
* Fix: Only paste raw token in Swagger

---

### 2. ❌ Putting Token in URL

* Mistake: Token was passed as `challenge_id`
* Fix: Token must be in Authorization header

---

### 3. ❌ MongoDB Connection Errors

* Issue: SSL handshake / connection failed
* Fix:

  * Added IP to MongoDB Atlas whitelist
  * Corrected connection string format

---

### 4. ❌ Async vs Sync MongoDB Calls

* Mistake: Used `find_one()` without `await`
* Fix: Use async Motor methods:

  ```python
  await collection.find_one()
  ```

---

### 5. ❌ Data Type Mismatch

* Issue: `ObjectId` vs string mismatch
* Fix: Store and query consistently as strings

---

### 6. ❌ Incorrect Field Names

* Mistake: `"progress value"` instead of `progress_value`
* Fix: Follow exact schema naming

---

### 7. ❌ Extra Quotes Bug (Critical)

* Stored:

  ```json
  ""challenge_id""
  ```
* Fix: Ensure clean string storage without extra quotes

---

### 8. ❌ bcrypt Password Limit Error

* Error: Password > 72 bytes
* Fix: Truncate password:

  ```python
  password = password[:72]
  ```

---

# 💡 Key Learnings

* Importance of consistent data types in NoSQL
* Proper JWT handling in APIs
* Async programming with FastAPI + Motor
* Debugging real backend production issues

---

# 🚀 Future Improvements

* Leaderboard system
* Daily streak tracking
* Role-based access (admin/user)
* Rate limiting
* Refresh tokens

---

# 👨‍💻 Author

**Ayush**
Backend Developer | AI/ML Enthusiast

---


# Register users
---------------

<img width="1836" height="642" alt="image" src="https://github.com/user-attachments/assets/db784f6d-5184-4457-a876-2061986c5984" />
<img width="1182" height="935" alt="image" src="https://github.com/user-attachments/assets/8fe6218f-0fc2-4316-b538-867828a3537d" />

# Login users
--------------

<img width="1370" height="901" alt="image" src="https://github.com/user-attachments/assets/7c94b6c3-0784-4b77-8cbf-2d2264e524d6" />
<img width="1297" height="293" alt="image" src="https://github.com/user-attachments/assets/26e68122-f5f1-4563-9223-a8c224400f55" />

# Get challeneges
-------------------

<img width="1290" height="560" alt="image" src="https://github.com/user-attachments/assets/81925b07-e6cd-4d45-9f2b-fc2f301ba09b" />
<img width="1379" height="434" alt="image" src="https://github.com/user-attachments/assets/effe0301-5a38-41a1-beaf-15258a5b7f5e" />
<img width="1395" height="855" alt="image" src="https://github.com/user-attachments/assets/b428228e-37aa-404e-8e73-02cd5c2a8854" />


# Post challenges
--------------------

<img width="1335" height="952" alt="image" src="https://github.com/user-attachments/assets/d1b07ec6-175f-4713-a651-8eafcaf5a3d9" />
<img width="1306" height="371" alt="image" src="https://github.com/user-attachments/assets/38ccc401-3238-44ce-8f05-7a8558319b36" />

# Join challenge
----------------
<img width="1051" height="318" alt="image" src="https://github.com/user-attachments/assets/dea829dd-4900-43e7-b231-e5a48c2cf4d9" />
<img width="1354" height="710" alt="image" src="https://github.com/user-attachments/assets/f493dd54-d6e2-4d53-81b8-13c25c393867" />
<img width="1245" height="713" alt="image" src="https://github.com/user-attachments/assets/2fae9f13-3d61-4d87-9662-3d8dc245bc1f" />



# Progress challenge
----------------------

<img width="1265" height="954" alt="image" src="https://github.com/user-attachments/assets/85907334-8a42-45ff-a6a0-fffee7cd185e" />
<img width="1045" height="375" alt="image" src="https://github.com/user-attachments/assets/201e4868-2ffe-4789-8e62-21c56a27323a" />
<img width="1904" height="630" alt="image" src="https://github.com/user-attachments/assets/b0adce3d-1e30-4935-89af-91eab0710ea9" />


