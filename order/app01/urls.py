from fastapi import APIRouter

user = APIRouter()


@user.get("user/users")
async def userList():
    return [{"message": "food"}]


@user.get("user/user/1")
async def userItem():
    return {"message": "bed"}
