from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.data_models import ModelBase, Room, House, Post
from datetime import datetime
import logging


def nuke_db(db_uri="I WILL NOT NUKE A DB BY DEFAULT ARE YOU INSANE???"):
    engine = create_engine(db_uri)
    logging.info(f"About to take off and nuke {db_uri} from orbit. IT'S THE ONLY WAY TO BE SURE!")
    ModelBase.metadata.drop_all(engine)


def initialize_orm(db_uri="sqlite:///myplace-db.sqlite"):
    engine = create_engine(db_uri)
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


def create_room(session, name):
    room = Room(1, "Parlour")
    session.add(room)
    session.commit()


