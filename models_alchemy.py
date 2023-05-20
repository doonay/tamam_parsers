from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    game_id = Column(String)
    title = Column(String)
    platforms = Column(ARRAY(String))
    base_price = Column(Integer)
    discounted_price = Column(Integer)
    discount = Column(Integer)
    img = Column(String)
    last_modified = Column(String)

    @classmethod
    def table_name(cls, company):
        return f'{company}_games'