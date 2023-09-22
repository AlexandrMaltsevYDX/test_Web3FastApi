from typing_extensions import Annotated
from pydantic import BaseModel, Field, EmailStr, field_validator
import re


class User(BaseModel):
    name: Annotated[str, Field(max_length=50)]
    surname: Annotated[str, Field(max_length=50)]
    email: EmailStr
    eth_address: str
    password: Annotated[str, Field(max_length=50)]

    @field_validator("eth_address")
    def val_eth_address(cls, value: str) -> str:
        cls.pattern = re.compile(r"^0x[0-9a-fA-F]{40}$")
        if not cls.pattern.match(value):
            raise ValueError(
                "Invalid Ethereum wallet address. It should start with '0x'"
                " followed by 40 hexadecimal characters."
                f"Password exceeds maximum length of {cls.max_length}"
            )
        return value

    @field_validator("password")
    def val_password(cls, value: str) -> str:
        cls.max_length = 8
        cls.pattern = re.compile(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{1,"
            + str(cls.max_length)
            + "}$"
        )

        if not cls.pattern.match(value):
            raise TypeError(
                "Password must be from Digits and Letters"
                f"Password length must be {cls.max_length} chars"
            )
        return value

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Bob",
                    "surname": "Johnson",
                    "email": "bob.johnson@example.com",
                    "eth_address": "0x0914B7665920386a9F05a53e83d1c999B25Eedb5",
                    "password": "BObpAS88",
                }
            ]
        }
    }


class Me(BaseModel):
    name: Annotated[str, Field(max_length=50)]
    surname: Annotated[str, Field(max_length=50)]
    email: EmailStr
    eth_address: Annotated[str, Field(max_length=50)]

    @field_validator("eth_address")
    def val_eth_address(cls, value: str) -> str:
        cls.pattern = re.compile(r"^0x[0-9a-fA-F]{40}$")
        if not cls.pattern.match(value):
            raise ValueError(
                "Invalid Ethereum wallet address. It should start with '0x'"
                " followed by 40 hexadecimal characters."
                f"Password exceeds maximum length of {cls.max_length}"
            )
        return value

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Bob",
                    "surname": "Johnson",
                    "email": "bob.johnson@example.com",
                    "eth_address": "0x0914B7665920386a9F05a53e83d1c999B25Eedb5",
                }
            ]
        }
    }


class UserSignature(BaseModel):
    user_id: int
    signature: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "user_id": "123",
                    "signature": "0xd46f930774942cd133304705cf20c0a44c02b13f470d3bd515f894d3570a86e269572dcf0b3139fb1c8bc1d0e3dd83f48b488b1547c1d875f506cb6a22a7a87a1b",
                }
            ]
        }
    }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    def val_password(cls, value: str) -> str:
        cls.max_length = 8
        cls.pattern = re.compile(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{1,"
            + str(cls.max_length)
            + "}$"
        )

        if not cls.pattern.match(value):
            raise TypeError(
                "Password must be from Digits and Letters"
                f"Password length must be {cls.max_length} chars"
            )
        return value

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "bob.johnson@example.com",
                    "password": "BObpAS88",
                }
            ]
        }
    }
