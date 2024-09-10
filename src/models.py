import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    
class Planet(Base):
    __tablename__ = 'planets'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)

class Character(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    heigth = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    brith_year = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicles'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    manufacturer = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    max_atmospheric_speed = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)

class Favorito(Base):
    __tablename__ = 'favoritos'
    
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey("users.id"))
    users = relationship(User)
    planet_id = Column(Integer, ForeignKey("planets.id"))
    planets = relationship(Planet)
    characters_id = Column(Integer, ForeignKey("characters.id"))
    characters = relationship(Character)
    vehicles_id = Column(Integer, ForeignKey("vehicles.id"))
    vehicles = relationship(Vehicle)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
