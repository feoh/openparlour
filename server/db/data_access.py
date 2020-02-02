from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.data_models import ModelBase, Room, BlockedRooms, House, Post
from datetime import datetime


def initialize_orm():
    engine = create_engine("sqlite:///myplace-db.sqlite")
    ModelBase.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def get_all_rooms(session):
    session = initialize_orm()
    all_rooms_query = session.query(Room).all()



def get_all_posts(session):
    session = initialize_orm()
    all_posts_query = session.query()


def create_post(session, room, date, title, body):
    post = Post(room="LivingRoom", date=datetime.now(), title=title, body=body)
    session.add(post)
    session.commit()
