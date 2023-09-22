from typing_extensions import Annotated
from fastapi import (
    FastAPI,
    Header,
    Depends,
)
from sqlalchemy.orm import Session
from . import services, models, schemas
from .database import SessionLocal, engine
from pydantic import EmailStr

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/sign_up")
def sign_up(
    privat_key_wallet: str,
    user: schemas.User,
    db: Session = Depends(get_db),
) -> schemas.UserSignature:
    response: (int, str) = services.sign_up(
        user=user,
        privat_key_wallet=privat_key_wallet,
        db=db,
    )
    user_signature = schemas.UserSignature(
        user_id=response[0],
        signature=response[1],
    )
    return user_signature


@app.get("/sign_in")
def sign_in(
    email: EmailStr,
    password: str,
    db: Session = Depends(get_db),
) -> str:
    user_sign_in = schemas.UserSignIn(email=email, password=password)
    response = services.authenticate(
        request=user_sign_in,
        db=db,
    )
    return response


@app.get("/user")
def user(
    Bearer: Annotated[str | None, Header()] = None,
    db: Session = Depends(get_db),
) -> schemas.Me:
    my_data: schemas.Me = services.get_user_by_token(Bearer=Bearer, db=db)
    return my_data
