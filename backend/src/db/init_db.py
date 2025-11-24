from sqlmodel import SQLModel
from backend.src.db.session import engine

def init_db():
    SQLModel.metadata.create_all(engine)
    