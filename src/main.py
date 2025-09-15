from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: str
    email:str

usuarios_db = [
        {"id": 1, "nome": "Eduardo", "email": "edu@gmail.com"},
        {"id": 2, "nome": "Ana", "email": "ana@gmail.com"},
        {"id": 3, "nome": "Maria", "email": "maria@gmail.com"}
]

@app.get("/")
def root():
    return {"message": "Hello World"}
@app.get("/usuarios")
def listar_usuarios():
    return usuarios_db

@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    usuarios_db.append(usuario.dict())
    return {"mensagem": "Usuário criado com sucesso", "usuario": usuario}

@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id:int):
    for u in usuarios_db:
      if u["id"] == usuario_id:
        return u
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

