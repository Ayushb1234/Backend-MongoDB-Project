from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserLogin
from app.db.database import users_collection
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth")

@router.post("/register")
async def register(user: UserCreate):

    existing_user = await users_collection.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(400, "User already exists")

    await users_collection.insert_one({
        "email": user.email,
        "password": hash_password(user.password),
        "role": "user"
    })

    return {"message": "User registered"}

@router.post("/login")
async def login(user: UserLogin):

    db_user = await users_collection.find_one({"email": user.email})

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(401, "Invalid credentials")

    token = create_access_token({
        "user_id": str(db_user["_id"]),
        "role": db_user["role"]
    })

    return {"access_token": token}