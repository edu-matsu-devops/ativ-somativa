from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/usuario")
def listar_usuarios():
    return [
        {"id": 1, "nome": "Eduardo"},
        {"id": 2, "nome": "Ana"},
        {"id": 3, "nome": "Maria"}
    ]
