from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from app.schemas.challenge import ChallengeCreate
from app.db.database import challenges_collection, user_challenges_collection
from app.dependencies.auth import get_current_user
from bson import ObjectId

router = APIRouter(prefix="/challenges")

@router.post("/")
def create_challenge(challenge: ChallengeCreate):
    challenges_collection.insert_one({
        **challenge.dict(),
        "is_active": True,
        "created_at": datetime.utcnow()
    })
    return {"message": "Challenge created"}

@router.get("/")
def get_challenges():
    return list(challenges_collection.find({"is_active": True}, {"_id": 0}))

@router.post("/{challenge_id}/join")
def join_challenge(challenge_id: str, user=Depends(get_current_user)):
    exists = user_challenges_collection.find_one({
        "user_id": user["user_id"],
        "challenge_id": challenge_id
    })

    if exists:
        raise HTTPException(400, "Already joined")

    user_challenges_collection.insert_one({
        "user_id": user["user_id"],
        "challenge_id": challenge_id,
        "joined_at": datetime.utcnow(),
        "progress": 0
    })

    return {"message": "Joined challenge"}