from fastapi import APIRouter

shop = APIRouter()


@shop.post("/shop/toy")
async def toy():
    return {"message": "toy"}


@shop.post("/shop/pillow")
async def pillow():
    return {"message": "pillow"}
