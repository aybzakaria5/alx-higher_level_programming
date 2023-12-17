#!/usr/bin/python3
"""creating tables and link it to the DB"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """ a class inherting from Base that creates a table
    with columns and links to the MySql db"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
