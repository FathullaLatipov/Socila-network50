from fastapi import APIRouter
from pydantic import BaseModel
from database.postservice import *
from datetime import datetime

from database import get_db

# Сделать все API