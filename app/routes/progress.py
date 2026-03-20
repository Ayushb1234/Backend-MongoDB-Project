from fastapi import APIRouter, Depends, HTTPException
from app.schemas.progress import ProgressUpdate
from app.db.database import user_challenges_collection
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/progress")


@router.post("/")
async def update_progress(data: ProgressUpdate, user=Depends(get_current_user)):

    # 🔍 check if user joined the challenge
    record = await user_challenges_collection.find_one({
        "user_id": user["user_id"],
        "challenge_id": data.challenge_id
    })

    if not record:
        raise HTTPException(status_code=404, detail="Not joined")

    # 📝 update progress
    await user_challenges_collection.update_one(
        {"_id": record["_id"]},
        {"$set": {"progress": data.progress_value}}
    )

    return {"message": "Progress updated"}