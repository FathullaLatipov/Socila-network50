from fastapi import APIRouter
from pydantic import BaseModel
from database.postservice import *
from datetime import datetime
from database.models import UserPost

from database import get_db

post_router = APIRouter(tags=['Управление постами'], prefix='/posts')


# Получить все посты
@post_router.get('/all_posts')
async def all_posts():
    db = next(get_db())
    posts = db.query(UserPost).all()
    return posts


# Получить определенный пост
@post_router.get('/exact_post')
async def get_post(id: int):
    exact_post = get_exact_post_db(id)
    return exact_post


# Изменение определенного поста
@post_router.post('/exact_post/edit')
async def change_post(id: int, new_text: str):
    data = change_post_db(id=id, new_text=new_text)
    return data


# Удалить определенный пост
@post_router.delete('/exact_post/delete')
async def delete_post(id: int):
    data = delete_post_db(id=id)
    return data


# Добавление поста
@post_router.post('/add')
async def add_post(user_id: int, main_text: str, description: str, hashtag: str):
    post = add_post_db(user_id, main_text, description, hashtag)
    return post


# Добавление комментария
@post_router.post('/add_comment')
async def public_comment(user_id: int, post_id: int, comment_text: str):
    comment = public_comment_db(user_id, post_id, comment_text)
    return comment


# Получить комментарии определенного поста
@post_router.get('/exact_post/comments')
async def exact_post_comment(post_id: int):
    comments = exact_post_comment_db(post_id)
    return comments


# Изменить определенный комметарий:
@post_router.put('/comment/edit')
async def change_comment_text(id: int, new_comment: str):
    changed_comment = change_comment_text_db(id, new_comment)
    return changed_comment


# Удалить определенного комментария
@post_router.delete('/comment/delete')
async def delete_exact_comment(id: int):
    delete_comment = delete_exact_comment_db(id)
    return delete_comment


# Получить все комменты
@post_router.get('/all_comments')
async def get_all_comments():
    comments = get_all_comments_db()
    return comments


# Рекомедация исходя из хэштега
@post_router.get('/hashtag/recommend')
async def get_recommend_hashtag(size: int, hashtag: str):
    recommend = get_recommend_hashtag_db(size, hashtag)
    return recommend


# Удаление определенного хэштега
@post_router.delete('/hashtag/delete')
async def delete_hashtag(hashtag_name: str):
    del_hashtag = delete_exact_hashtag(hashtag_name=hashtag_name)
    return del_hashtag


# Получить все хэштеги
@post_router.get('/all_hashtags')
async def all_hashtags():
    hashtags = get_all_hashtags()
    return hashtags
