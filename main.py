from fastapi import FastAPI
from database import Base, engine
from roots import empresa

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(empresa.router)
