from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relatioship

Base = declarative_base()

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(String)
    rating = Column(String)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    genre = relationship("Genre", back_populates="books")
    
engine = create_engine('sqlite:///data/books.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
