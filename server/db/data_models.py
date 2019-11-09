from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

ModelBase = declarative_base()


class Rooms(ModelBase):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


# The basic unit of communication in MyHouse is the Post.
class Posts(ModelBase):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    room = relationship(Rooms)
    date = Column(DateTime)
    title = Column(String, unique=True)
    body = Column(String)


class BlockedRooms(ModelBase):
    room = relationship(Rooms)


class House(ModelBase):
    address = Column(String, primary_key=True)
    blocked_rooms = relationship(BlockedRooms)



