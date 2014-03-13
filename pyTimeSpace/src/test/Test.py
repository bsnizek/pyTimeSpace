'''
Created on Mar 13, 2014

@author: Bernhard Snizek
'''

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String

from sqlalchemy.dialects.postgresql import TIMESTAMP

from geoalchemy2.types import Geography

from sqlalchemy.ext.declarative import declarative_base

import datetime

Base = declarative_base()

class Dot(Base):
    __tablename__ = 'dots'
    gid = Column(Integer, primary_key=True)
    geography = Column(Geography(geometry_type='POINT', srid=4326))
    time = Column('time', TIMESTAMP)
    
    def __init__(self, geography, time):
        self.geography = geography
        self.time = time
    
class Tracjectory(Base):
    __tablename__ = 'trajectories'
    gid = Column(Integer, primary_key=True)
    geography = Column(Geography(geometry_type='POLYLINE', srid=4326))

class Test:
    
    def __init__(self):
        
        self.meta = MetaData()
        self.engine = None
        self.dots_table = None
        self.connection = None
        
    def setup(self):
        
        self.dots_table = Table('dots', self.meta,
                            Column('gid', Integer, primary_key=True),
                            Column('geography', Geography(geometry_type='POINT', srid=4326)),
                            Column('time', TIMESTAMP)
                            )
        
        self.engine = create_engine('postgresql://abm:abm@localhost:5432/dots', echo=True)
        
        print self.engine
        
        self.connection = self.engine.connect()
        
        # smid nogle punkter ind 
        
    def add_some_points(self):
        timestamp_one = datetime.datetime(1,2,3) 
        
    def test_query(self):
        result = self.engine.execute(self.dots_table.select())
        for row in result:
            print row

if __name__ == '__main__':
    test = Test();
    test.setup()
    test.add_some_points();
