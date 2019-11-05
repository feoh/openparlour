from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

ModelBase = declarative_base()

# The basic unit of communication in MyHouse is the Post.
class Posts(ModelBase):
    __tablename__ = "posts"
    room = relationship(Room)
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    subject = Column(String, unique=True)
    body = Column(String)


class Rooms(ModelBase):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    posts = relationship(Posts, backref="posts")


class BlockedRooms(ModelBase):
    room = relationship(Rooms)


class House(ModelBase):
    address = Column(String, primary_key=True)
    blocked_rooms = relationship(BlockedRooms)



