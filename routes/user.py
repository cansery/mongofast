from fastapi import APIRouter

from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity
from bson.objectid import ObjectId

user = APIRouter()

@user.get('/')
async def find_all_users():
    return usersEntity(conn.first.user.find())

@user.get('/{id}')
async def find_one_user(id):
    return userEntity(conn.first.user.find_one({"_id": ObjectId(id)}))

@user.post('/')
async def create_user(user: User):
    conn.first.user.insert_one(dict(user))
    return userEntity(conn.first.user.find_one({"_id": user._id}))

@user.put('/{id}')
async def create_user(id, user: User):
    conn.first.user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })
    return userEntity(conn.first.user.find_one({"_id": ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id):
    return userEntity(conn.first.user.find_one_and_delete({"_id": ObjectId(id)}))
    
    