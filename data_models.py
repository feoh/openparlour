from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

sqlbase = declarative_base()

def init_sql():
    engine = create_engine('sqlite:///:memory:', echo=True)
    return engine


class Post(sqlbase):
    __tablename__ = "posts"
    room = Column(String)
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    subject = Column(String, unique=True)
    body = Column(String)



