import hmac
import time
import base64
import string
import secrets
from hashlib import sha256

class TokenGenerator:
    def __init__(self):
        pass

    def header_generate(self):
        header = """{"alg": "HS256", "typ": "jwt"}"""
        return self._safe_base64_url_encode(header)

    def payload_generate(self, username: str, permission: str):
        # Example methods
        exp = round(time.time()) + 50
        payload = """{"iss": "Avimitin Studio", "exp": "%d", "user": "%s", "admin": "%s"}""" % (exp, username, permission)
        return self._safe_base64_url_encode(payload)

    @staticmethod
    def encrypt(key, msg):
        sign = hmac.new(key, msg, sha256).digest()
        return sign

    def generate(self, username, permission):
        key = self._secret_key_generate(16)
        print("加密密钥： " + key.decode("utf-8"))
        message = self.header_generate() + b"." + self.payload_generate(username, permission)
        signature = self.encrypt(key, message)
        signature_b64 = self._safe_base64_url_encode(signature)
        part = [message, signature_b64]
        return b".".join(part).decode("utf-8")

    @staticmethod
    def _secret_key_generate(len: int):
        current_time = round(time.time())
        combine_text = string.ascii_letters + str(current_time)
        salt = ""
        while len > 0:
            salt += secrets.choice(combine_text)
            len -= 1
        return salt.encode("utf-8")

    @staticmethod
    def _safe_base64_url_encode(text):
        if isinstance(text, str):
            text = text.encode("utf-8")
        elif isinstance(text, bytes):
            pass
        else:
            raise TypeError("Expected string or bytes but got others")

        text_b64 = base64.urlsafe_b64encode(text)
        return text_b64.replace(b"=", b"")


if __name__ == "__main__":
    u = TokenGenerator()
    print(u.generate("avimitin", "True"))
