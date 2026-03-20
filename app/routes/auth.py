from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserLogin
from app.db.database import users_collection
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth")

@router.post("/register")
def register(user: UserCreate):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(400, "User already exists")

    users_collection.insert_one({
        "email": user.email,
        "password": hash_password(user.password)
    })

    return {"message": "User registered"}

@router.post("/login")
def login(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(401, "Invalid credentials")

    token = create_access_token({"user_id": str(db_user["_id"])})
    return {"access_token": token}