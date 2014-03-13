'''
Created on Mar 13, 2014

@author: besn
'''

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String


class Test:
    
    def __init__(self):
        
        
        meta = MetaData()
        
        dots_table = Table('users', meta,
                            Column('id', Integer, primary_key=True),
                            Column('name', String(50))
                            )
        
        engine = create_engine('postgresql://abm:abm@localhost:5432/abm', echo=True)
        
        print engine
        
        connection = engine.connect()
        
        result = engine.execute(dots_table.select())
        for row in result:
            print row

if __name__ == '__main__':
    test = Test();
