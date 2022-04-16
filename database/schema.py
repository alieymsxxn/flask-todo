import os
from datetime import datetime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, DateTime, Integer, create_engine, ForeignKey

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
url = 'sqlite:///'+os.path.join(BASE_DIR, 'site.db')

Base = declarative_base()
engine = create_engine(url=url)
Session = sessionmaker()


class User(Base):
    
    __tablename__ = 'user'
    
    id = Column(Integer(), primary_key=True)
    username =  Column(String(15), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.utcnow)
    password = Column(String(100), nullable=False, unique=True)
    
    def __repr__(self):
        return f"<User username='{self.username}' email='{self.email}'>"


class ToDo(Base):
    
    __tablename__ = 'todo'
    
    id = Column(Integer(), primary_key=True)
    user =  Column(Integer, ForeignKey('user.id'))
    content =  Column(String, nullable=False)
    date_created = Column(DateTime(), default=datetime.utcnow)
    
    def __repr__(self):
        return f"<ToDo user_id='{self.user}'>"

    
    def dictify(self):

        dictified = {}
        for key in ToDo.__table__.columns.keys():
            dictified.update({ key : str(getattr(self, key)) })
        
        return dictified

