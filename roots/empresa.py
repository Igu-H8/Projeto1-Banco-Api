from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Empresa
from schemas import EmpresaCreate, EmpresaOut
from database import get_db

router = APIRouter()

@router.post("/empresas", response_model=EmpresaOut)
def criar_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = Empresa(**empresa.model_dump())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@router.get("/empresas", response_model=list[EmpresaOut])
def listar_empresas(db: Session = Depends(get_db)):
    return db.query(Empresa).all()

@router.get("/empresas/{id}", response_model=EmpresaOut)
def obter_empresa(id: int, db: Session = Depends(get_db)):
    empresa = db.query(Empresa).filter(Empresa.id == id).first()
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return empresa

@router.delete("/empresas/{id}")
def deletar_empresa(id: int, db: Session = Depends(get_db)):
    empresa = db.query(Empresa).filter(Empresa.id == id).first()
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    db.delete(empresa)
    db.commit()
    return {"ok": True}
