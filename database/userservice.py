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


# DarkPrice
# Логин        hello@gmail.com, DarkPrice
def login_user(email, password):
    db = next(get_db())
    user_email = db.query(User).filter_by(email=email).first()  # hello@gmail.com
    # user_password = db.query(User).filter_by(password=password).first()
    print(user_email)
    if user_email:
        if user_email.password == password:
            return user_email.id
        else:
            return 'Неправильные данные(('
    else:
        return 'Нету такого email'


# Получение данных определенного пользователя
# profile/3
def get_profile_db(user_id):
    db = next(get_db())
    user_info = db.query(User).filter_by(user_id=user_id).first()
    if user_info:
        return user_info
    return False


# Изменения данных пользователя   email         hello2@gmail.com
def change_user_data_db(user_id, change_info, new_info):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        try:
            if change_info == 'name':
                user.name = new_info
                db.commit()
                return 'Success changed'
            elif change_info == 'city':
                user.city = new_info
                db.commit()
                return 'Success changed'
            elif change_info == 'email':
                user = db.query(User).filter_by(email=new_info).first()
                if user:
                    return 'This email is already in use'
                else:
                    user.email = new_info
                    db.commit()
                    return 'Success changed!'
        except:
            return 'Нету такого значения для изменения'
    return False


# Удаления пользователя Logout
def delete_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return 'Success deleted'
    return False
