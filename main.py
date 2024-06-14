from fastapi import FastAPI

from api.user_api.users import user_router

from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)