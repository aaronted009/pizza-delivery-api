from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()


# validation schema
class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 0,  # TODO : find a better way to do this (id is supposed to be optional)
                    "username": "janedoe",
                    "email": "janedoe@gmail.com",
                    "password": "password",
                    "is_staff": False,
                    "is_active": True,
                }
            ]
        }
    }


class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv("AUTH_SECRET_KEY")


class LoginModel(BaseModel):
    username: str
    password: str