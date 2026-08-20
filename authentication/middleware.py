from channels.middleware import BaseMiddleware
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs

@database_sync_to_async
def get_user(token_string):
    try:
        UntypedToken(token_string)
    except (InvalidToken, TokenError) as e:
        return AnonymousUser()
    
    from rest_framework_simplejwt.authentication import JWTAuthentication
    try:
        user = JWTAuthentication().get_user(UntypedToken(token_string))
        return user
    except Exception:
        return AnonymousUser()

class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        query_string = parse_qs(scope["query_string"].decode())
        token = query_string.get("token")
        
        if token:
            scope["user"] = await get_user(token[0])
        else:
            scope["user"] = AnonymousUser()
            
        return await super().__call__(scope, receive, send)

def JWTAuthMiddlewareStack(inner):
    return JWTAuthMiddleware(inner)
