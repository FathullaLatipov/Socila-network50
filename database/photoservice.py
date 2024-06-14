from database import get_db
from database.models import PostPhoto
from datetime import datetime


# Загрузка изображений для поста
def add_photo_db(post_id, photo_path):
    db = next(get_db())
    photo = PostPhoto(post_id=post_id, photo_path=photo_path,
                      reg_date=datetime.now())
    db.add(photo)
    db.commit()
    return f'Успешно добавлен для этого {post_id}'


# Вернуть все изображения
def get_all_photos():
    db = next(get_db())
    all_photos = db.query(PostPhoto).all()
    return all_photos
