import hmac
import time
import base64
import string
import secrets
from hashlib import sha256

class TokenGenerator:
    def __init__(self, key:str=None, **kwargs):
        """
        :params kwargs: Input set of predefined claims which are not mandatory but recommended, 
        to provide a set of useful, interoperable claims. Some of them are: iss (issuer), exp 
        (expiration time), sub (subject), aud (audience), and others. For more you can explore
        RFC 7519 Standard: https://tools.ietf.org/html/rfc7519
        """
        self.encrypt_key = key

        result = self._generate(kwargs)
        self._JWT = result.get("JWT")
        self._salt = result.get("salt")
        self._signature = result.get("sign")
    
    def token(self):
        """
        :return JWT: return a base64 encrypt token
        """
        return self._JWT
    
    def key(self):
        """
        :return salt: return a key use to encrypt message
        """
        return self._salt

    def sign(self):
        """
        :return signature: return only the last part of the token
        """
        return self._signature

    def _header_generate(self):
        header = """{"alg": "HS256", "typ": "jwt"}"""
        return self._safe_base64_url_encode(header)

    def _payload_generate(self, payload: dict):
        if not isinstance(payload, dict):
            raise TypeError("Expected dict but got %s" % type(payload))
        # Example methods
        payload_str = str(payload)
        return self._safe_base64_url_encode(payload_str)

    @staticmethod
    def _encrypt(key, msg):
        sign = hmac.new(key, msg, sha256).digest()
        return sign

    def _generate(self, payload: dict):
        key = self._secret_key_generate(16)
        message = self._header_generate() + b"." + self._payload_generate(payload)
        signature = self._encrypt(key, message)
        signature_b64 = self._safe_base64_url_encode(signature)
        part = [message, signature_b64]
        JWT = b".".join(part).decode("utf-8")
        return {"JWT":JWT, "salt":key.decode("utf-8"), "sign": signature_b64.decode("utf-8")}

    def _secret_key_generate(self, len: int):
        if self.encrypt_key:
            return self.encrypt_key.encode("utf-8")

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
    u = TokenGenerator(name="avimitin", iss="avimitin studio")
    print(u.token())
    print(u.key())
    print(u.sign())
