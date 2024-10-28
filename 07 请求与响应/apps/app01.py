from fastapi import APIRouter
from uuid import UUID

app01 = APIRouter()


@app01.get("/user/{id}")
async def user(id: str):
    # 0ecefc89-1a9c-4c3f-bf59-ddc2345f5c22
    print("id", id, type(id))
    try:
        UUID(id)
    except ValueError:
        return {"error": "Invalid UUID format"}

    return {"user_id": id, "message": "Hello User"}


@app01.get("/order/{id}")
async def user(id: int):
    print("id", id, type(id))

    return {"order_id": id, "message": "Hello User"}
