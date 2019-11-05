from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def initialize_orm():
    engine: Engine = create_engine("sqlite:///myplace-db.sqlite")
    data_models.ModelBase.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def get_all_rooms(session):
    session = initialize_orm()
    all_rooms_query = session.query()
