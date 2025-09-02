from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/usuarios")
def listar_usuarios():
    return [
        {"id": 1, "nome": "Eduardo", "email": "edu@gmail.com"},
        {"id": 2, "nome": "Ana", "email": "ana@gmail.com"},
        {"id": 3, "nome": "Maria", "email": "maria@gmail.com"}
    ]
