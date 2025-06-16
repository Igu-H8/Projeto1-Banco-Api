from pydantic import BaseModel

class EmpresaCreate(BaseModel):
    name: str
    cnpj: str
    endereco: str
    email: str
    telefone: str | None = None

class EmpresaOut(EmpresaCreate):
    id: int

    class Config:
        orm_mode = True
