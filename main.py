from fastapi import FastAPI
from users.user_api import user_router
from health.health_api import health_router

from database import Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(health_router)
