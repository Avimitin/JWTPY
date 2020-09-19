# JWTPY

## Info

Use this modules to generate a Token following [JSON Web Token](https://jwt.io/)(JWT) Standard ([RFC 7519](https://tools.ietf.org/html/rfc7519)) exactly.

## Usage

```python
from JWT import TokenGenerator
g = TokenGenerator()
# example
g.generate("avimitin", "admin")
```

## Customize

You can change [arguments](https://tools.ietf.org/html/rfc7519#section-4.1) of the payload and generate methods:

```python
# you can change the arguments and payload
def payload_generate(self, username: str, *args):
    # Example methods
    exp = round(time.time()) + 50
    payload = """{"iss": "Your Studio", "exp": "%d", "user": "%s", "others": "%s"}""" % (exp, username, args)
    return self._safe_base64_url_encode(payload)
```

and don't forget to change the generate method's arguments.