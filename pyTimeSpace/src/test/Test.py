'''
Created on Mar 13, 2014

@author: besn
'''

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String

from sqlalchemy.dialects.postgresql import TIMESTAMP

from geoalchemy2.types import *


class Test:
    
    def __init__(self):
        
        meta = MetaData()
        
        dots_table = Table('dots', meta,
                            Column('gid', Integer, primary_key=True),
                            Column('geography', Geography(geometry_type='POINT', srid=4326)),
                            Column('time', TIMESTAMP)
                            )
        
        engine = create_engine('postgresql://abm:abm@localhost:5432/dots', echo=True)
        
        print engine
        
        connection = engine.connect()
        
        result = engine.execute(dots_table.select())
        for row in result:
            print row

if __name__ == '__main__':
    test = Test();
