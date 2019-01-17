from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Workplaces(Base):
	__tablename__= "workplaces"
	id = Column(Integer,primary_key= True)
	name = Column(String)
	agelimit = Column(Integer)
	location = Column(String)
	phonenumber = Column(Integer)
	description = Column(String)

 
