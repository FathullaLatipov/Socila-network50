from database.models import User
from database import get_db
from datetime import datetime


# Проверка наличия имени,номера и тд
def check_user_db(name, email, phone_number):
    db = next(get_db())
    checker_name = db.query(User).filter_by(name=name).first()
    checker_email = db.query(User).filter_by(email=email).first()
    checker_phone_number = db.query(User).filter_by(phone_number=phone_number).first()
    if checker_name:
        return "Такой Username уже занят"
    elif checker_email:
        return "Такой email уже занят"
    elif checker_phone_number:
        return "Такой номер телефона уже занят"
    else:
        return True


# Регистрация пользователя
def register_user(name, email, phone_number, password, user_city=None, birthday=None, status=None):
    db = next(get_db())
    checker = check_user_db(name, email, phone_number)
    if checker:
        new_user = User(name=name, email=email, phone_number=phone_number, password=password,
                        user_city=user_city, birthday=birthday, status=status,
                        reg_date=datetime.now()
                        )
        db.add(new_user)
        db.commit()
        return f'Вот новый пользователь и его ИД {new_user.id}'
    else:
        checker

