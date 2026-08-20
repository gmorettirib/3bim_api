# models.py

from sqlalchemy import Column, Integer, String, Float
from database import Base

class ProdutoDB(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)

class timeDB(Base):
    __tablename__ = 'time'
    id = Column(Integer, primary_key=True, index=True)
    time = Column(String(200), nullable=False)
    tecnico = Column(String(100), nullable=False)
    artilheiro = Column(String(100), nullable=False)
    gols = Column(Float, nullable=False)