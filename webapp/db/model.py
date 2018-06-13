import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, Integer, DateTime,
    String, Table, ForeignKey
)
from sqlalchemy.orm import relationship

from webapp import app

Base = declarative_base()

registration_table = Table('registration', Base.metadata,
    Column('event_name_key', String(255), ForeignKey('event.name_key')),
    Column('team_number', Integer, ForeignKey('team.number'))
)

class Event(Base):
    __tablename__ = 'event'
    name_key = Column(String(255), primary_key=True)
    common_name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    season = Column(Integer, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    teams = relationship('Team', secondary=registration_table, back_populates='events')
    matches = relationship('Match', back_populates='event')

    def __repr__(self):
        return "<Team(name_key={name_key}, common_name={common_name}, season={season})>".format(
                name_key=self.name_key, common_name=self.common_name, address=self.address,
                season=self.season, start_date=self.start_date, end_date=self.end_date
            )


class Match(Base):
    __tablename__ = 'match'
    match_number = Column(Integer, primary_key=True)
    event_name = Column(String(255), primary_key=True)
    red_1_num = Column(Integer, ForeignKey('team.number'), nullable=False)
    red_2_num = Column(Integer, ForeignKey('team.number'), nullable=False)
    red_3_num = Column(Integer, ForeignKey('team.number'), nullable=False)
    blue_1_num = Column(Integer, ForeignKey('team.number'), nullable=False)
    blue_2_num = Column(Integer, ForeignKey('team.number'), nullable=False)
    blue_3_num = Column(Integer, ForeignKey('team.number'), nullable=False)
    score_red = Column(Integer)
    score_blue = Column(Integer)

    event_name_key = Column(Integer, ForeignKey('event.name_key'), nullable=False)
    event = relationship('Team', back_populates='matches')
    red_1 = relationship('team')
    red_2 = relationship('team')
    red_3 = relationship('team')
    blue_1 = relationship('team')
    blue_2 = relationship('team')
    blue_3 = relationship('team')

    def __repr__(self):
        return "<Match(match_number={match_number}, event_name={event_name}, " \
            "red_alliance=[{red_1}, {red_2}, {red_3}]," \
            "blue_alliance=[{blue_1}, {blue_2}, {blue_3}])>".format(
                match_number=self.match_number, event_name=self.event_name,
                red_1=self.red_1_num, red_2=self.red_2_num, red_3=self.red_3_num,
                blue_1=self.blue_1_num, blue_2=self.blue_2_num, blue_3=self.blue_3_num
            )


class Team(Base):
    __tablename__ = 'team'
    number = Column(Integer, primary_key=True)
    formal_name = Column(String(500), nullable=False)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)

    events = relationship('Event', secondary=registration_table, back_populates='teams')

    def __repr__(self):
        return "<Team(number={number}, name={name}, address={address}".format(
            number=self.number, name=self.name, address=self.address
        )
