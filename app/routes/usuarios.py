from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.usuario import UsuarioCreate, UsuarioUpdate
from app.models.usuario import Usuario as UsuarioModel
from app.database import SessionLocal

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_db = UsuarioModel(
        nome=usuario.nome,
        email=usuario.email,
        idade=usuario.idade
    )

    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)

    return {
        "mensagem": "Usuário salvo no banco",
        "id": usuario_db.id
    }


@router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(UsuarioModel).all()
    return usuarios


@router.get("/{usuario_id}")
def buscar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = (
        db.query(UsuarioModel)
        .filter(UsuarioModel.id == usuario_id)
        .first()
    )

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    return usuario


@router.delete("/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = (
        db.query(UsuarioModel)
        .filter(UsuarioModel.id == usuario_id)
        .first()
    )

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    db.delete(usuario)
    db.commit()

    return {"mensagem": "Usuário deletado com sucesso"}


@router.put("/{usuario_id}")
def atualizar_usuario(
    usuario_id: int,
    usuario: UsuarioUpdate,
    db: Session = Depends(get_db)
):
    usuario_db = (
        db.query(UsuarioModel)
        .filter(UsuarioModel.id == usuario_id)
        .first()
    )

    if not usuario_db:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    usuario_db.nome = usuario.nome
    usuario_db.email = usuario.email
    usuario_db.idade = usuario.idade

    db.commit()
    db.refresh(usuario_db)

    return usuario_db
