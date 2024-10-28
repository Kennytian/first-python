from fastapi import FastAPI
import uvicorn

from apps.app01 import app01
from apps.app02 import app02

app = FastAPI()

app.include_router(app01, prefix="/app01", tags=["01 路径参数"])
app.include_router(app02, prefix="/app02", tags=["02 查询参数"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=2222, reload=True)
