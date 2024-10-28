from typing import Union, Optional

from fastapi import APIRouter

app02 = APIRouter()


@app02.get("/jobs/{keyword}")
async def jobs(
    keyword: str,
    education_level: Union[str, None] = None,
    experience: Optional[int] = None,
):
    return {
        "job_id": 1,
        "message": "Hello job",
        "keyword": keyword,
        "education_level": education_level,
        "experience": experience,
    }
