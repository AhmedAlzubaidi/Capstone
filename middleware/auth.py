import json
from flask import request, redirect, session
from functools import wraps
from jose import JWT
from urllib.request import urlopen

AUTH0_DOMAIN = 'dev-ci5z6zo4.eu.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'Capstone'


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    result = request.headers['Authorization']

    if not result:
        raise AuthError({
            'code': 'bad_request',
            'description': 'no token is provided'
        }, 400)

    result = result.split(' ')

    if len(result) != 2 or result[0] != 'Bearer':
        raise AuthError({
            'code': 'bad_request',
            'description': 'token has wrong format'
        }, 400)

    return result[1]


def check_permissions(permission, payload):
    if 'permissions' not in payload:
        raise AuthError({
            'code': 'bad_request',
            'description': 'payload does not contain permissions'
        }, 400)

    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'no_permission',
            'description': 'role does not have sufficient permissions'
        }, 401)

    return True


def verify_decode_jwt(token):
    jsonurl = urlopen("https://" + AUTH0_DOMAIN + "/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())
    unverified_header = JWT.get_unverified_header(token)
    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }

    if rsa_key:
        try:
            return JWT.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer="https://" + AUTH0_DOMAIN + "/"
            )
        except JWT.ExpiredSignatureError:
            raise AuthError({"code": "token_expired",
                             "description": "token is expired"}, 401)
        except JWT.JWTClaimsError:
            raise AuthError({"code": "invalid_claims",
                             "description":
                                 "incorrect claims, \
                                 please check the audience and issuer"}, 401)
        except Exception:
            raise AuthError({"code": "invalid_header",
                             "description":
                                 "Unable to parse authentication \
                                  token."}, 401)


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'profile' not in session:
            # Redirect to Login page here
            return redirect('https://dev-ci5z6zo4.eu.auth0.com/authorize?response_type=token&audience=Capstone&client_id=m9aIZpy47lGy9nMTkk6sa64LNU1QTUTK&redirect_uri=http/localhost/blogs')
        return f(*args, **kwargs)

    return decorated