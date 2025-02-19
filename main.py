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
empresa = []
acessoria = []
# ----------

# empresa
@app.post("/cad_empresa/", response_model=Empresa)
def create_item(empresas: Empresa):
    
    if any(existing_empresas.id == empresas.id for existing_empresas in empresa):
        raise HTTPException(status_code=400, detail="ID já existe")
    
    if any(existing_empresas.cnpj == empresas.cnpj for existing_empresas in empresa):
        raise HTTPException(status_code=400, detail="CNPJ já existe")
    
    empresa.append(empresas)
    return empresas



# MENSSGAEN DE TESTE
@app.get("/")
def teste():
    return "A api esta no ar!"
# ------------------

if __name__ == "__main__":
    run(app, port=8000)
