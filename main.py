# Versão 1.7
from fastapi import FastAPI
from database import Base, engine
from roots import empresa, acessoria

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(empresa.router)
app.include_router(acessoria.router)
