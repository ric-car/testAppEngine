"""
Primary FastPI ASGI application

"""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import google.appengine.api
from app.api.endpoints import api_routes


def create_app():
    # Initialize FastAPI app
    app1 = FastAPI()

    # Enable CORS via middleware
    app1.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_headers=['*'],
        allow_methods=['*'],
        allow_origins=['*'],
    )

    app1.include_router(api_routes)

    return app1

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield b'Hello world!\n'
 
app = google.appengine.api.wrap_wsgi_app(app)
application = create_app()
