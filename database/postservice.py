from database import get_db
from .models import UserPost, Comment, Hashtags
from datetime import datetime


# Получить всех постов
def get_all_posts():
    db = next(get_db())
    posts = db.query(UserPost).all()
    return posts


# Получить определенный пост
def get_exact_post_db(id: int):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(id=id).first()
    if exact_post:
        return exact_post
    return 'Нету такого поста('


# Изменить определенный пост
def change_post_db(id, new_text):
    db = next(get_db())
    post_to_edit = db.query(UserPost).filter_by(id=id).first()
    if post_to_edit:
        post_to_edit.main_text = new_text
        db.commit()
        return 'Success changed!'
    return False


# Удалить определнный пост
def delete_post_db(id):
    db = next(get_db())
    post_to_delete = db.query(UserPost).filter_by(id=id).first()
    if post_to_delete:
        db.delete(post_to_delete)
        db.commit()
        return 'Success deleted'
    return 'Нету такого поста('


# Добавления поста
def add_post_db(user_id, id, main_text, descriptions, hashtag=None):
    db = next(get_db())
    if user_id:
        new_post = UserPost(user_id=user_id, id=id, main_text=main_text,
                            descriptions=descriptions, reg_date=datetime.now(),
                            hastag=hashtag
                            )
        db.add(new_post)
        db.commit()
        return 'Success created'
    return 'Такого пользователя нету Ока('


# Добавления комментария
def public_comment_db(user_id, id, comment_text):
    db = next(get_db())
    if user_id and id:
        new_comment = Comment(user_id=user_id, id=id, comment_text=comment_text)
        db.add(new_comment)
        db.commit()
        return 'Успешно добавлено комментария'
    return 'Нету такого поста либо пользователя(('


# Получить комментарии определенного поста
def get_exact_post_comment_db(post_id):
    db = next(get_db())
    exact_comments = db.query(Comment).filter_by(post_id=post_id).all()
    if exact_comments:
        return exact_comments
    return False


# Изменить текст в комментарии
def change_comment_text_db(id, new_text):
    db = next(get_db())
    comment_edit = db.query(Comment).filter_by(id=id).first()
    if comment_edit:
        comment_edit.comment_text = new_text
        db.commit()
        return 'Успешно изменен'
    return False


# Удаления определенного комментария
def delete_exact_comment_db(id):
    db = next(get_db())
    comment_delete = db.query(Comment).filter_by(id=id).first()
    if comment_delete:
        db.delete(comment_delete)
        db.commit()
        return 'Успешно удалено'
    return False


# Создание хештега #
def add_hashtag(hashtag_name):
    db = next(get_db())
    new_hashtag = Hashtags(hashtag_name=hashtag_name, reg_date=datetime.now())
    db.add(new_hashtag)
    db.commit()
    return True


# Рекомендация исходя из хэштега  Обьяснить на след уроке ученикам
def get_recommend_hashtag(size, hashtag_name):
    db = next(get_db())
    posts = db.query(UserPost).filter_by(hashtag_name=hashtag_name).limit(size).all()
    return posts

# ДЗ!!!!
# Получение определенного хэштега
def get_exact_hashtag(hashtag_name):
    db = next(get_db())
    exact_hashtag = db.query(Hashtags).filter_by(hashtag_name=hashtag_name).first()
    if exact_hashtag:
        return exact_hashtag
    return 'Нет такого хэштега'


# Получить все хэштеги
def get_all_hashtags():
    db = next(get_db())
    hashtags = db.query(Hashtags).all()
    return hashtags


# Удаление определенного хэштега
def delete_exact_hashtag(hashtag_name):
    db = next(get_db())
    delete_hashtag = db.query(Hashtags).filter_by(hashtag_name=hashtag_name).first()
    if delete_hashtag:
        db.delete(delete_hashtag)
        db.commmit()
        return 'Хэштег удален'
    return 'Нет такого хэштега :('


# Внутри userservice.py дописать изменения данных пользователя например password,... кроме email!!
