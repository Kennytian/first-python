from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "Kenny"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2019-06-01 12:22",
    "friends": [1, 2, "3"],
    "name": "Kenny",
}

user = User(**external_data)
print(user.id)

print(repr(user.signup_ts))

print(user.friends)

print(user.model_dump())
print(user.model_dump_json())
