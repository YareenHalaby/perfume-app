from sqlalchemy import Column ,Integer ,Float,String ,ARRAY,Boolean
from dataBase import Base
from sqlalchemy import DateTime

class Perfume(Base):
    __tablename__ ="perfumes"
    id= Column(Integer,primary_key=True ,index=True)
    name = Column(String,nullable=False)
    scentIds=Column(ARRAY(Integer),nullable=False)
    brand = Column(String,nullable=False)
    fragrance_notes=Column(String,nullable=False)
    price=Column(Float,nullable=False)
    volume=Column(Integer,nullable=False)
    image_url=Column(String,nullable=True)
    buy_url=Column(String,nullable=False)
    deleted = Column(Boolean, default=False) # Soft delete flag 
    deleted_on = Column(DateTime, nullable=True) # Stores deletion timestamp



   