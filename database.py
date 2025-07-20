from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.auto_approve
premium_users = db.premium_users

def is_premium(user_id: int) -> bool:
    return premium_users.find_one({"user_id": user_id}) is not None

def add_premium(user_id: int):
    premium_users.insert_one({"user_id": user_id})

def remove_premium(user_id: int):
    premium_users.delete_one({"user_id": user_id})

def count_users():
    return premium_users.count_documents({})
