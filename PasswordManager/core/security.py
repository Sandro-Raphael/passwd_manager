import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class Security:

    def __init__(self, key: bytes):
        self.key = key
        self.aes = AESGCM(key)

    def encrypt(self, plaintext: str) -> bytes:

        nonce = os.urandom(12)

        ciphertext = self.aes.encrypt(
            nonce,
            plaintext.encode(),
            None
        )

        return nonce + ciphertext

    def decrypt(self, encrypted_data: bytes) -> str:

        nonce = encrypted_data[:12]
        ciphertext = encrypted_data[12:]

        plaintext = self.aes.decrypt(
            nonce,
            ciphertext,
            None
        )

        return plaintext.decode()