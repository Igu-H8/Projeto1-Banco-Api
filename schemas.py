from pydantic import BaseModel


# schemas empresas
class EmpresaCreate(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str | None = None


class EmpresaOut(EmpresaCreate):
    id_empresas: int
    class Config:
        orm_mode = True


# schemas acessorias
class AcessoriaCreate(BaseModel):
    nome: str
    periodicidade: str
    empresas_id: int

class AcessoriasOut(AcessoriaCreate):
    id_acessorias: int
    class Config:
        orm_mode = True
