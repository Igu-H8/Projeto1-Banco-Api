# Versão 1.4
import uvicorn
import typing
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Empresa(BaseModel):
    id: int
    name: str
    cnpj: str
    endereco: str
    email: str
    telefone: str 


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
def create_empresa(empresa: Empresa):
    empresas.append(empresa)
    return empresa


@app.get("/empresa/{empresa_id}", response_model=Empresa)
def get_empresa(empresa_id: int):
    for empresa in empresas:
        if empresa.id == empresa_id:
            return empresa
    raise HTTPException(status_code=404, detail="empresa não encontrada")


@app.put("/empresa/{empresa_id}", response_model=Empresa)
def update_empresa(empresa_id: int, updated_empresa: Empresa):
    for index, empresa in enumerate(empresas):
        if empresa.id == empresa_id:
            empresas[index] = updated_empresa
            return updated_empresa
    raise HTTPException(status_code=404, detail="Empresa não encontrada")


# MENSSGAEN DE TESTE
@app.get("/")
def teste():
    return "A api esta no ar!"
# ------------------

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
