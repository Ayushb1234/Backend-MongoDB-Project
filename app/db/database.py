from pymongo import MongoClient
from app.core.config import MONGO_URL, DB_NAME

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

users_collection = db["users"]
challenges_collection = db["challenges"]
user_challenges_collection = db["user_challenges"]