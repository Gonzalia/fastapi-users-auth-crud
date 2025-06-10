from fastapi import FastAPI
from routes import auth_routes, user_route
from models.user import Base
from db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_routes.router, prefix="/api", tags=["Auth"])
app.include_router(user_route.router, prefix="/api", tags=["Users"])

