from sqlalchemy.orm import Session

from . import models, schemas, utils


def create_user(db: Session, user: schemas.User):
    db_user = models.User(
        name=user.name,
        surname=user.surname,
        email=user.email,
        eth_address=user.eth_address,
        password=user.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_token(db: Session, user_id: int):
    token = utils.generate_token(user_id, "secret")
    db_token = models.Token(
        user_id=user_id,
        token=token,
    )
    db.add(db_token)
    db.commit()


def get_token_by_user(db: Session, user_email: str, password: str) -> str:
    user = (
        db.query(models.User).filter(models.User.email == user_email).first()
    )
    if user.password == password:
        token = (
            db.query(models.Token)
            .filter(models.Token.user_id == user.id)
            .first()
        )
        return token.token
    return ""


def get_user_by_token(db: Session, token: str):
    user_id = (
        db.query(models.Token)
        .filter(models.Token.token == token)
        .first()
    )

    print(user_id.user_id)
    user = db.query(models.User).filter(models.User.id == user_id.user_id).first()
    return user
