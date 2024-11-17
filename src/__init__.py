from fastapi import FastAPI
from src.books.routes import book_router
from src.db.db import init_db
from src.auth.routes import auth_router
from src.reviews.routes import review_router
from .middleware import register_middleware

version = 'v1'

app = FastAPI(title='Book', description="REST API for a book", version=version)

register_middleware(app)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=["auth"])
app.include_router(review_router, prefix=f"/api/{version}/reviews", tags=["reviews"])


