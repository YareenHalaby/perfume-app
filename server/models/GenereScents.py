from sqlalchemy import Column ,Integer,String,ARRAY
from dataBase import Base

class Scents(Base):
    __tablename__="Scents"
    id=Column(Integer,primary_key=True, index=True)
    name=Column(String,nullable=False)