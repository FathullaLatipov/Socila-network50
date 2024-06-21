#photo.py
from fastapi import APIRouter, Request, Body, UploadFile, File
from database.photoservice import add_photo_db, get_all_photos_db

photo_router = APIRouter(tags=['Изображения'], prefix='/photos')


# Загрузка изображения
@photo_router.post('/add_photo')
async def add_photo(post_id: int, photo_path: UploadFile = File(...)):
    if photo_path:
        # hello_1.jpg
        with open(f'database/photos/photo_{post_id}.jpg', 'wb') as photo:
            # read - hello_1.jpg
            photo_to_save = await photo_path.read()
            photo.write(photo_to_save)
            add_photo_db(post_id, f'database/photos/photo_{post_id}.jpg')
        return {'status': 1, 'message': 'Success'}
    else:
        return {'status': 0, 'message': 'Empty'}


# Получить все изображения ДЗ

