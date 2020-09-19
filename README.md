# JWTPY

## Info

Use this modules to generate a Token following [JSON Web Token](https://jwt.io/)(JWT) Standard ([RFC 7519](https://tools.ietf.org/html/rfc7519)) exactly.

## Usage

```python
from JWT import TokenGenerator
# follow the standard of rfc7519
g = TokenGenerator(name="avimitin", iss="avimitin Studio", exp=time.time()+60)
# return JWT token
g.token()
# return encrypt key
g.key()
# return the signature
g.sign()
```

## Payload Standard

Extract some standard:

```text
"iss" (Issuer) Claim

   The "iss" (issuer) claim identifies the principal that issued the
   JWT.  The processing of this claim is generally application specific.
   The "iss" value is a case-sensitive string containing a StringOrURI
   value.  Use of this claim is OPTIONAL.

"sub" (Subject) Claim

   The "sub" (subject) claim identifies the principal that is the
   subject of the JWT.  The claims in a JWT are normally statements
   about the subject.  The subject value MUST either be scoped to be
   locally unique in the context of the issuer or be globally unique.
   The processing of this claim is generally application specific.  The
   "sub" value is a case-sensitive string containing a StringOrURI
   value.  Use of this claim is OPTIONAL.

"aud" (Audience) Claim

   The "aud" (audience) claim identifies the recipients that the JWT is
   intended for.  Each principal intended to process the JWT MUST
   identify itself with a value in the audience claim.  If the principal
   processing the claim does not identify itself with a value in the
   "aud" claim when this claim is present, then the JWT MUST be
   rejected.  In the general case, the "aud" value is an array of case-
   sensitive strings, each containing a StringOrURI value.  In the
   special case when the JWT has one audience, the "aud" value MAY be a
   single case-sensitive string containing a StringOrURI value.  The
   interpretation of audience values is generally application specific.
   Use of this claim is OPTIONAL.

"exp" (Expiration Time) Claim

   The "exp" (expiration time) claim identifies the expiration time on
   or after which the JWT MUST NOT be accepted for processing.  The
   processing of the "exp" claim requires that the current date/time
   MUST be before the expiration date/time listed in the "exp" claim.

   Implementers MAY provide for some small leeway, usually no more than
   a few minutes, to account for clock skew.  Its value MUST be a number
   containing a NumericDate value.  Use of this claim is OPTIONAL.
```

[More information](https://tools.ietf.org/html/rfc7519#section-4.1)
