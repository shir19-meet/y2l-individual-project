from models import*

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite://database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def save_to_database(name,age,location,phone,description):
	new_workplace = Workplaces(
		name = name,
		age = age,
		location = location,
		phone = phone,
		description = description)
	session.add(new_workplace)
	session.commit()