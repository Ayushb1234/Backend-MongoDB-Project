from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("your_mongo_url")

print("Connected")