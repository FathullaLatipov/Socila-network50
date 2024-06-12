from fastapi import FastAPI
from passlib.context import CryptContext

from database import Base, engine
Base.metadata.create_all(bind=engine)

SECRET_KEY = 'ufuebi4bisdb830b92yb919b91!bf09'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 200

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

app = FastAPI(docs_url='/')

