from fastapi import FastAPI


from app01.urls import user
from app02.urls import shop

app = FastAPI()

app.include_router(user, tags=["app01的标签"])
app.include_router(shop, tags=["app02的标签"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
