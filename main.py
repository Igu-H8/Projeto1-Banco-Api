import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def teste():
    return "A api esta no ar!"


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
