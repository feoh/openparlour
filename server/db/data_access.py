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


def add_commit_refresh(session, thing):
    session.add(thing)
    session.commit()
    session.refresh(thing)


def get_all_rooms(session):
    all_rooms_query = session.query(Room).all()


def get_post_by_id(session, id):
    single_post_query = session.query(Post).filter(Post.id == id)
    return list(single_post_query)


def get_all_posts(session):
    all_posts_query = session.query(Post).all()
    return list(all_posts_query)


def create_post(session, room, date, title, body):
    post = Post(room=room, date=datetime.now(), title=title, body=body)
    add_commit_refresh(session, post)
    return post.id


def create_room(session, name):
    room = Room(1, name)
    add_commit_refresh(session, room)
    return room.id


def create_house(session, address):
    house = House(id=1, address="http://nyi.nyi")
    add_commit_refresh(session, house)
    return house.id