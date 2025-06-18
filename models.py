from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base 


class Empresa(Base):
    __tablename__ = "empresas"

    id_empresas = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cnpj = Column(String(14), nullable=False)
    endereco = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=True)

    # estudar a utilidade desse código
    # acessorias = relationship("Acessoria", back_populates="empresas")


class Acessoria(Base):
    __tablename__ = "acessorias"

    id_acessorias = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    periodicidade = Column(String(100), nullable=False)
    empresas_id = Column(Integer, ForeignKey("empresas.id_empresas"),
                          nullable=False)
    
    # estudar a utilidade desse código
    # empresas = relationship("Empresa", back_populates="acessorias")
