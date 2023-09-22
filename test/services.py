from . import schemas, repositories, utils
from sqlalchemy.orm import Session


def sign_up(user: schemas.User, db: Session, privat_key_wallet: str):
    user_obj = repositories.create_user(db, user)
    response = utils.user_id_to_ethereum_message(
        user_obj.id, privat_key_wallet
    )
    repositories.create_token(user_id=user_obj.id, db=db)
    return response


def authenticate(request: schemas.UserSignIn, db: Session) -> str:
    response = repositories.get_token_by_user(
        user_email=request.email,
        password=request.password,
        db=db,
    )
    return response


def get_user_by_token(Bearer: str, db: Session):
    user = repositories.get_user_by_token(db=db, token=Bearer)
    me = schemas.Me(
        name=user.name,
        surname=user.surname,
        email=user.email,
        eth_address=user.eth_address,
    )
    return me
