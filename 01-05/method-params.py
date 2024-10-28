from tkinter.constants import FALSE

from fastapi import FastAPI

app = FastAPI()


@app.get(
    "/products",
    tags=["所有产品"],
    summary="这是摘要",
    description="描述",
    response_description="返回产品列表",
    deprecated=FALSE,
)
async def get_products():
    return [
        {
            "id": 1,
            "name": "Product 1",
            "price": 100,
            "description": "This is product 1",
        },
        {
            "id": 2,
            "name": "Product 2",
            "price": 200,
            "description": "This is product 2",
        },
    ]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("method-params:app", host="127.0.0.1", port=8000, reload=True)
