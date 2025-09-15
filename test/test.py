import pytest
from src.main import *
from fastapi import HTTPException

def test_root():
    result = root()
    assert result == {"message": "Hello World"}


def test_listar_usuarios():
    usuarios = listar_usuarios()
    assert isinstance(usuarios, list)
    assert len(usuarios) >= 3
    assert usuarios[0]["nome"] == "Eduardo"

def test_criar_usuario():
    novo_usuario = Usuario(id=4, nome="João", email="joao@gmail.com")
    resposta = criar_usuario(novo_usuario)
    assert resposta["mensagem"] == "Usuário criado com sucesso"
    assert resposta["usuario"].nome == "João"
    assert any(u["id"] == 4 for u in usuarios_db)


def test_buscar_usuario():
    usuario = buscar_usuario(1)
    assert usuario["nome"] == "Eduardo"
    assert usuario["email"] == "edu@gmail.com"

def test_buscar_usuario_inesitente():
    with pytest.raises(HTTPException) as exc:
        buscar_usuario(10)

    assert exc.value.status_code == 404
    assert exc.value.detail == "Usuário não encontrado"
