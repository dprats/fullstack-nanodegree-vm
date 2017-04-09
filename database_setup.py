# 1. CONFIGURATION
import sys
from sqlalchemy import 
Column, ForeignKey, Integer, String
# used for configuration and class code
from sqlalchemy.ext.declarative import
declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# 2. CLASS
# Representation of the table as a python class
# extends the Base class(instantiated above)

#We create two classes, corresponding with the two tables we want in our database
#Table 1
class Restaurant(Base):

	#We use the __{{name}}__ syntax to let SQLAlchemy know the variable
	#We will use to refer to our table.
	#For conventional purposes we use lowercase with underscore
	__tablename__ = 'restaurant'

	#3. MAPPER
	# Maps python objects to columns in the database
	#syntax: 
	#{{columnName}} = Column(attributes...) 
	name = Column(
		String(80), nullable = False)

	id = Column(
		Integer, primary_key = True)


#Table 2
class MenuItem(Base):

	__tablename__ = 'menu_item'

	#Mapper
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	course = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	restaurant_id = Column(
		Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)

#END OF FILE
engine = create_engine(
	'sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)