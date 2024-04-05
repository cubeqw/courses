from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    bonuces = Column(Integer)

class CourseModel(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String)
    image = Column(String)
    description = Column(String)
    price = Column(Integer)