from model import*

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def save_to_database(name,age,location,phone,description):
	new_workplace = Workplaces(
		name = name,
		agelimit = age,
		location = location,
		phonenumber = phone,
		description = description)
	session.add(new_workplace)
	session.commit()

def get_all_workplaces():
    workplaces = session.query(Workplaces).all()
    return workplaces