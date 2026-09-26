import base64
import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


AES_KEY = os.getenv("AES_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")


if not AES_KEY:
    raise ValueError("AES_KEY não foi configurada no arquivo .env")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL não foi configurada no arquivo .env")


try:
    AES_KEY = base64.urlsafe_b64decode(AES_KEY)
except Exception as error:
    raise ValueError("AES_KEY possui formato inválido") from error


if len(AES_KEY) != 32:
    raise ValueError("AES_KEY precisa possuir 32 bytes")