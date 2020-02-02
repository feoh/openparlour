from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

ModelBase = declarative_base()


class Room(ModelBase):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


# The basic unit of communication in MyHouse is the Post.
class Post(ModelBase):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    room = relationship(Room)
    date = Column(DateTime)
    title = Column(String, unique=True)
    body = Column(String)

    def to_json(self):
        return {
            'id': self.id,
            'room': self.room,
            'date': self.date,
            'title': self.title,
            'body': self.body
        }


class BlockedRooms(ModelBase):
    id = Column(Integer, primary_key=True)
    rooms = relationship(Room)

    def to_json(self):
        return {
            'id': self.id,
            'rooms': self.rooms
        }


class House(ModelBase):
    id = Column(Integer, primary_key=True)
    address = Column(String, primary_key=True)
    blocked_rooms = relationship(BlockedRooms)

    def to_json(self):
        return {
            'id': self.id,
            'address': self.address,
            'blocked_rooms': self.blocked_rooms
        }


