from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

ModelBase = declarative_base()


class Room(ModelBase):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


# The basic unit of communication in MyHouse is the Post.
class Post(ModelBase):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    room = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    title = Column(String, unique=True)
    body = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'room': self.room,
            'date': self.date,
            'title': self.title,
            'body': self.body
        }


class House(ModelBase):
    __tablename__ = "houses"
    id = Column(Integer, primary_key=True)
    address = Column(String, primary_key=True)

    def to_dict(self):
        return {
            'id': self.id,
            'address': self.address,
        }


