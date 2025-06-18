from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Acessoria
from schemas import AcessoriaCreate, AcessoriasOut
from database import get_db

router = APIRouter()


@router.post("/acessorias", response_model=AcessoriasOut)
def criar_acessoria(acessoria: AcessoriaCreate, db: Session = Depends(get_db)):
    db_acessoria = Acessoria(**acessoria.model_dump())
    db.add(db_acessoria)
    db.commit()
    db.refresh(db_acessoria)
    return db_acessoria


@router.get("/acessorias", response_model=list[AcessoriasOut])
def listar_acessoria(db: Session = Depends(get_db)):
    return db.query(Acessoria).all()


@router.get("/acessorias/{id}", response_model=AcessoriasOut)
def obter_acessoria(id: int, db: Session = Depends(get_db)):
    acessoria = db.query(Acessoria).filter(Acessoria.id_acessorias == id).first()
    if not acessoria:
        raise HTTPException(status_code=404, detail="Acessoria não encontrada")
    
    return acessoria


@router.put("/acessorias/{id}", response_model=AcessoriasOut)
def atualizar_acessoria(id: int, acessoria: AcessoriaCreate, db: Session = Depends(get_db)):
    db_acessoria = db.query(Acessoria).filter(Acessoria.id_acessorias == id).first()
    if not db_acessoria:
        raise HTTPException(status_code=404, detail="Assessoria não encontrada")
    
    for key, value in acessoria.model_dump().items():
        setattr(db_acessoria, key, value)

    db.commit()
    db.refresh(db_acessoria)
    return db_acessoria


@router.delete("/acessorias/{id}")
def deletar_acessoria(id: int, db: Session = Depends(get_db)):
    acessoria = db.query(Acessoria).filter(Acessoria.id_acessorias == id).first()
    if not Acessoria:
        raise HTTPException(status_code=404, detail="Acessoria não encontrada")
    
    db.delete(acessoria)
    db.commit()
    return {"ok": True}
