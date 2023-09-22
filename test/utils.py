from web3 import Web3
from web3.auto import w3
from eth_account import Account
from jose import jwt


def hash_user_id(user_id: int) -> str:
    # Преобразование user_id в uint256
    user_id_bytes = user_id.to_bytes(32, byteorder="big")
    user_id_hex = Web3.to_hex(user_id_bytes)

    # Хеширование в Keccak256
    user_id_hash = Web3.keccak(hexstr=user_id_hex)

    return Web3.to_hex(user_id_hash)


def hash_to_ethereum_signed_message(hash_hex: str) -> str:
    # Преобразование хеша в бинарный вид
    hash_bytes = bytes.fromhex(hash_hex[2:])  # Исключаем префикс "0x"

    # Формирование Ethereum Signed Message
    message = b"\x19Ethereum Signed Message:\n32" + hash_bytes

    eth_hash = w3.keccak(message)

    return w3.to_hex(eth_hash)


def sign_ethereum_message(eth_hash: str, private_key: str) -> str:
    # Преобразование хеша в бинарный вид
    eth_hash_bytes = bytes.fromhex(eth_hash[2:])

    # Подпись Ethereum Signed Message приватным ключом
    signed_message = Account.signHash(eth_hash_bytes, private_key=private_key)
    signature = signed_message.signature.hex()

    return signature


def user_id_to_ethereum_message(
    user_id: int,
    private_key: str,
) -> (int, str):
    user_hash = hash_user_id(user_id)
    eth_hash = hash_to_ethereum_signed_message(user_hash)
    signature = sign_ethereum_message(eth_hash, private_key)
    return (user_id, signature)


def generate_token(
    user_id: int,
    secret,
) -> str:
    token = jwt.encode(
        {"user_id": user_id},
        secret,
        algorithm="HS256",
    )
    return token


# ethHash:0x43dddc6fa8c46dff6aa09673625c5a9edc8ab273727e7c97202a550d60e7d927
# Хеширование сообщения

# user_id = 123
# test = "0x5569044719a1ec3b04d0afa9e7a5310c7c0473331d13dc9fafe143b2c4e8148a"
