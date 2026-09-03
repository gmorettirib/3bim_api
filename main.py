from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, get_db
from models import ProdutoDB, timeDB
from schemas import ProdutoCreate, ProdutoResponse, timeResponse, timeCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
def criar_tabelas():
    Base.metadata.create_all(bind=engine)
    
def buscar_time(db: Session, filme_id: int):
    return db.query(timeDB).filter(timeDB.id == time_id).first()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GET /produtos/{id}
@app.get('/produtos/{id}', response_model=ProdutoResponse)
def obter_produto(
    id: int,    
    db: Session = Depends(get_db)
):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == id).first()

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail='Produto não encontrado'
        )

    return produto


# POST /produtos
@app.post('/produtos', response_model=ProdutoResponse, status_code=201)
def criar_produto(
    produto: ProdutoCreate,
    db: Session = Depends(get_db)
):
    novo_produto = ProdutoDB(**produto.model_dump())

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto


# DELETE /produtos/{id}
@app.delete('/produtos/{id}', status_code=204)
def remover_produto(
    id: int,
    db: Session = Depends(get_db)
):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == id).first()

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail='Produto não encontrado'
        )

    db.delete(produto)
    db.commit()


# PUT /produtos/{id}
@app.put('/produtos/{id}', response_model=ProdutoResponse)
def atualizar_produto(
    id: int,
    dados: ProdutoCreate,
    db: Session = Depends(get_db)
):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == id).first()

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail='Produto não encontrado'
        )

    produto.nome = dados.nome
    produto.preco = dados.preco
    produto.quantidade = dados.quantidade

    db.commit()
    db.refresh(produto)

    return produto

@app.get('/produtos', response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = db.query(ProdutoDB).all()
    return produtos


# ***** SEÇÃO ATIVIDADE 02 *****

# GET /time/{id}
@app.get('/time/{id}', response_model=timeResponse)
def obter_time(
    id: int,    
    db: Session = Depends(get_db)
):
    time = db.query(timeDB).filter(timeDB.id == id).first()

    if time is None:
        raise HTTPException(
            status_code=404,
            detail='time não encontrado'
        )

    return time


# POST /time
@app.post('/time', response_model=timeResponse, status_code=201)
def cadastrar_time(
    time: timeCreate,
    db: Session = Depends(get_db)
):
    novo_time = timeDB(**time.model_dump())

    db.add(novo_time)
    db.commit()
    db.refresh(novo_time)

    return novo_time


# DELETE /time/{id}
@app.delete('/time/{id}', status_code=204)
def remover_time(
    id: int,
    db: Session = Depends(get_db)
):
    time = db.query(timeDB).filter(timeDB.id == id).first()

    if time is None:
        raise HTTPException(
            status_code=404,
            detail='time não encontrado'
        )

    db.delete(time)
    db.commit()


# PUT /time/{id}
@app.put('/time/{id}', response_model=timeResponse)
def atualizar_time(
    id: int,
    dados: timeCreate,
    db: Session = Depends(get_db)
):
    time = db.query(timeDB).filter(timeDB.id == id).first()

    if time is None:
        raise HTTPException(
            status_code=404,
            detail='time não encontrado'
        )

    time.time = dados.time
    time.tecnico = dados.tecnico
    time.artilheiro = dados.artilheiro
    time.gols = dados.gols

    db.commit()
    db.refresh(time)

    return time

@app.get('/time', response_model=list[timeResponse])
def listar_times(db: Session = Depends(get_db)):
    times = db.query(timeDB).all()
    return times