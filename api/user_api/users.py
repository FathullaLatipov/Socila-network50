from fastapi import APIRouter, Request
from pydantic import BaseModel
from database.userservice import *
from datetime import datetime
from typing import Optional
from database.models import User
from database import get_db


class UserValidator(BaseModel):
    name: str
    phone_number: str
    email: str
    birthday: Optional[str] = None
    user_city: Optional[str] = None
    status: Optional[str] = None
    password: str


#     Руслан если ты это смотришь то напиши в группу то что это 15 строка!
user_router = APIRouter(tags=['Управления юзерами'], prefix='/users')


# Регистрация
@user_router.post('/api/registration')
async def register_user(validator: UserValidator):
    db = next(get_db())
    user_data = validator.dict()
    user_email = user_data.get('email')
    print(user_email)
    checker = db.query(User).filter_by(email=user_email).first()
    print(f'вроде ошибка {checker}')
    if not checker:
        try:
            reg_user = register_user_db(**user_data)
            print('Success')
            return {'status': 1, "message": reg_user}
        except Exception as e:
            print('Error')
            return {'status': 0, "message": str(e)}
    else:
        return {'status': 0, 'message': "Invalid email(("}


# Логин пользователя
@user_router.post('/api/login')
async def login_user_api(email, password):
    user = login_user(email=email, password=password)
    return user


# Получить определенного пользователя
@user_router.get('/api/user')
async def get_user(id: int):
    exact_user = get_profile_db(id)
    return exact_user


# Измененния данных пользователя
@user_router.put('/api/change_account')
async def change_user_profile(id: int, change_info: str, new_info: str):
    data = change_user_data_db(id=id, change_info=change_info, new_info=new_info)
    return data


# Удаление пользователя
@user_router.delete('/api/delete_user')
async def delete_user(id: int):
    data = delete_user_db(id=id)
    return data


@user_router.get('/all-users')
async def all_users():
    db = next(get_db())
    users = db.query(User).all()
    return users
