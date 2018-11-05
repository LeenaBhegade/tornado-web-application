from sqlalchemy import Integer, Column, String, LargeBinary
from tornado_sqlalchemy import (SessionMixin, as_future, declarative_base,
                                make_session_factory)

DeclarativeBase = declarative_base()

class Word(DeclarativeBase):
    __tablename__ = 'words'

    word_hash = Column(String(100), primary_key=True)
    word = Column(LargeBinary, unique=True)
    count = Column(Integer)