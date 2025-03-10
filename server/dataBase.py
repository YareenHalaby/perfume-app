from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os  

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Yareen2006%21@db:5435/perfume_db")  # Provide a default if the environment variable is not set

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()  # In case of error, roll back the transaction
        print(f"Error during DB operation: {e}")
    finally:
        db.close()
