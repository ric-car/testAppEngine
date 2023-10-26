"""
Primary API route endpoints

"""
from google.appengine.api.urlfetch import Fetch, GET
from fastapi import APIRouter
from starlette.responses import RedirectResponse

# Init FastAPI router for API endpoints
api_routes = APIRouter()


@api_routes.get('/')
def redirect_to_docs():
    """Redirect to API docs when at site root"""
    return RedirectResponse('/redoc')


@api_routes.get('/hello/{name}')
async def get_hello(name: str = 'world')-> dict:
    response = Fetch('https://httpbin.org/basic-auth/user/pass',method=GET)
    return dict(hello=name,code=response.status_code,content=response.content)
