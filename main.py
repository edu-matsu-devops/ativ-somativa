from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/usuarios")
def listar_usuarios():
    return usuarios_db

class Usuario(BaseModel):
    id: int
    nome: str
    email:str

usuarios_db = [
        {"id": 1, "nome": "Eduardo", "email": "edu@gmail.com"},
        {"id": 2, "nome": "Ana", "email": "ana@gmail.com"},
        {"id": 3, "nome": "Maria", "email": "maria@gmail.com"}
]

@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    usuarios_db.append(usuario.dict())
    return {"mensagem": "Usuário criado com sucesso", "usuario": usuario}
