from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from app.schemas.challenge import ChallengeCreate
from app.db.database import challenges_collection, user_challenges_collection
from app.dependencies.auth import get_current_user
from bson import ObjectId

router = APIRouter(prefix="/challenges")


# ✅ Create Challenge (Admin ideally)
@router.post("/")
async def create_challenge(challenge: ChallengeCreate):
    await challenges_collection.insert_one({
        **challenge.dict(),
        "is_active": True,
        "created_at": datetime.utcnow()
    })
    return {"message": "Challenge created"}


# ✅ Get Active Challenges
@router.get("/")
async def get_challenges():
    challenges = []
    
    async for c in challenges_collection.find({"is_active": True}):
        c["_id"] = str(c["_id"])   # convert ObjectId → string
        challenges.append(c)

    return challenges


# ✅ Join Challenge
@router.post("/{challenge_id}/join")
async def join_challenge(challenge_id: str, user=Depends(get_current_user)):

    # 🔍 check if already joined
    exists = await user_challenges_collection.find_one({
        "user_id": user["user_id"],
        "challenge_id": challenge_id
    })

    if exists:
        raise HTTPException(status_code=400, detail="Already joined")

    # 📝 insert join record
    await user_challenges_collection.insert_one({
        "user_id": user["user_id"],
        "challenge_id": challenge_id,
        "joined_at": datetime.utcnow(),
        "progress": 0
    })

    return {"message": "Joined challenge"}