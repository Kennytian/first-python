import os
from typing import Union, Optional

from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel

app = FastAPI()

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
ACCESS_KEY = os.getenv("ACCESS_KEY")
# print(f"ACCESS_KEY is: {ACCESS_KEY}")


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


# 注意：在外部请求是不能写在 access_key，要写成 Access-Key 或 access-key
async def verify_token(access_key: Optional[str] = Header(None)):
    if access_key != ACCESS_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")
    return access_key


@app.get("/protected")
async def read_protected(token: str = Depends(verify_token)):
    return {"msg": "You have access"}


@app.get("/")
async def read_root():
    return {"msg": "Say hello world using Python!"}


@app.get("/items/{item_id}")
async def read_item(
    item_id: int, q: Union[str, None] = None, token: str = Depends(verify_token)
):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, token: str = Depends(verify_token)):
    return {"item_name": item.name, "item_id": item_id}
