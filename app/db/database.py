from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.MONGO_URL)
db = client[settings.DB_NAME]

users_collection = db["users"]
challenges_collection = db["challenges"]
user_challenges_collection = db["user_challenges"]