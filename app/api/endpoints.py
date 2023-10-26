"""
Primary API route endpoints

"""
from fastapi import APIRouter
from starlette.responses import RedirectResponse
from google.auth.transport import requests


# Init FastAPI router for API endpoints
api_routes = APIRouter()
firebase_request_adapter = requests.Request()

@api_routes.get('/')
def redirect_to_docs():
    """Redirect to API docs when at site root"""
    return RedirectResponse('/redoc')


@api_routes.get('/hello/{name}')
async def get_hello(name: str = 'world')-> dict:
    response = requests.get('https://httpbin.org/basic-auth/user/pass')
    return dict(hello=name,code=response.status_code,content=response.content)
