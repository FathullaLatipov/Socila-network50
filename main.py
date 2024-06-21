from fastapi import FastAPI

from api.post_api.posts import post_router
from api.user_api.users import user_router
from api.photo_api.photo import photo_router


from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(post_router)
app.include_router(photo_router)