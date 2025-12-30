from fastapi import APIRouter
from app.schemas.usuario import Usuario

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.post("/")
def criar_usuario(usuario: Usuario):
    return {
        "mensagem": "Usuário criado com sucesso",
        "usuario": usuario
    }
