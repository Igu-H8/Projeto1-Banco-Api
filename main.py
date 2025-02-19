# Versão 1.1

from uvicorn import run
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Empresa(BaseModel):
    id: int
    name: str
    cnpj: int
    endereco: str
    email: str
    telefone: int


class Acessoria(BaseModel):
    id: int
    name: str
    periodicidade: str
    empresas_id: int


# Temporario
empresas = []
acessorias = []
# ----------


@app.post("/empresa/", response_model=Empresa)
def create_item(empresa: Empresa):
    
    if any(existing_empresa.id == empresa.id for existing_empresa in empresas):
        raise HTTPException(status_code=400, detail="ID já existe")
    
    if any(existing_empresa.cnpj == empresa.cnpj for existing_empresa in empresas):
        raise HTTPException(status_code=400, detail="CNPJ já existe")
    
    empresas.append(empresas)
    return empresas


@app.get("/empresa/", response_model=List[Empresa])
def get_items():
    return empresas


# MENSSGAEN DE TESTE
@app.get("/")
def teste():
    return "A api esta no ar!"
# ------------------

if __name__ == "__main__":
    run(app, port=8000)
