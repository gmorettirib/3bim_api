# schemas.py

from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    quantidade: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int

class timeBase(BaseModel):
    time: str
    tecnico: str
    artilheiro: str
    gols: float

class timeCreate(timeBase):
    pass

class timeResponse(timeBase):
    id: int

class Config:
    from_attributes = True