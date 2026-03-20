from fastapi import APIRouter, HTTPException
from datetime import datetime

from app.schemas.user import UserCreate, UserLogin
from app.db.database import users_collection
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth")


# ✅ REGISTER
@router.post("/register")
async def register(user: UserCreate):

    # 🔍 check if user exists
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 📝 insert user
    await users_collection.insert_one({
        "email": user.email,
        "password": hash_password(user.password),
        "role": "user",   # ✅ default role
        "created_at": datetime.utcnow()
    })

    return {"message": "User created"}


# ✅ LOGIN
@router.post("/login")
async def login(user: UserLogin):

    # 🔍 find user
    db_user = await users_collection.find_one({"email": user.email})

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # 🔐 verify password
    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # 🎟️ create JWT token
    token = create_access_token({
        "user_id": str(db_user["_id"]),
        "role": db_user.get("role", "user")   # safe fallback
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }