from fastapi import FastAPI
from fastapi import HTTPException

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
@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id:int):
    usuarios = [
        {"id": 1, "nome": "Eduardo", "email": "edu@gmail.com"},
        {"id": 2, "nome": "Ana", "email": "ana@gmail.com"},
        {"id": 3, "nome": "Maria", "email": "maria@gmail.com"}
    ]
    for u in usuarios:
        if u["id"] == usuario_id:
            return u
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

