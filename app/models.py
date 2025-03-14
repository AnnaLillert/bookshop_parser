from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@db:5432/books"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Genre(Base):  # Пример класса Genre
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    books = relationship("Book", back_populates="genre")

class Book(Base):  # Определение класса Book
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(Float)
    rating = Column(Integer)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    genre = relationship("Genre", back_populates="books"

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
