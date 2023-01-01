from sqlalchemy import Column, Date, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql+pymysql://db_user:admin@192.168.1.100:9906/register')
session_factory = sessionmaker(bind = engine)
Session = scoped_session(session_factory)

# Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

class RegisterTable(Base):
   __tablename__ = 'tbl_register'
   # id = Column(Integer, primary_key = True)
   first_name = Column('first_name', String(255))
   middle_name = Column('middle_name', String(255))
   last_name = Column('last_name', String(255))
   roll_number = Column('roll_number', String(255), primary_key = True)
   email = Column('email', String(255))
   phone_number = Column('phone_number', String(255))
   created_at = ('created_at',Date)

class CountTable(Base):
   __tablename__ = 'tbl_count'
   id = Column('id',Integer,primary_key = True)
   count = Column('count',Integer)


def checkdRecords(bar_code):
   session = Session()
   qry = session.query(RegisterTable).all()
   for record in qry:
      roll_num = record.roll_number
      if roll_num == bar_code:
         print('Matched : ', roll_num)
         session.close()
         return True
      # print(record.first_name, '\t', roll_num )
   session.close()
   return False

def getCount():
   session = Session()
   qry = session.query(CountTable).all()
   session.close()
   return int(qry[0].count)

def setCount(to_set):
   session = Session()
   qry = session.query(CountTable).all()
   qry[0].count = to_set
   session.commit()
   session.close()