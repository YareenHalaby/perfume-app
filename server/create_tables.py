from dataBase import engine ,Base
from models.perfumeModels import Perfume
from models.GenereScents import Scents

print("Creating all tables...")
Base.metadata.create_all(bind=engine)
