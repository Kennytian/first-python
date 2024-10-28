from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"user_id": 1, "message": "Hello World"}


@app.get("product")
async def product():
    return {"product_id": 1, "message": "Hello Product"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("quick-start:app", host="127.0.0.1", port=8000, reload=True)
