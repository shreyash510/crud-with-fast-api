from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def test(db: Session):
    data = db.query(models.User).all()
    return data


#create a new user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, lastname=user.lastname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
   
     
# dupdate user
def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        return None

    db_user.email = user.email
    db_user.lastname = user.lastname

    db.commit()
    db.refresh(db_user)
    return db_user

# delete a user
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        return None

    db.delete(db_user)
    db.commit()
    return db_user

