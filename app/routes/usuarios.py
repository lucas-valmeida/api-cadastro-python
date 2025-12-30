from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.usuario import UsuarioCreate, UsuarioUpdate
from app.models.usuario import Usuario as UsuarioModel
from app.database import SessionLocal

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


# 🔹 Dependência do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔹 Função auxiliar: buscar usuário por e-mail
def get_usuario_por_email(db: Session, email: str):
    return (
        db.query(UsuarioModel)
        .filter(UsuarioModel.email == email)
        .first()
    )


# =========================
# 📌 CRIAR USUÁRIO
# =========================
@router.post("/")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):

    # 🔎 Validação de e-mail único
    usuario_existente = get_usuario_por_email(db, usuario.email)

    if usuario_existente:
        raise HTTPException(
            status_code=400,
            detail="E-mail já cadastrado"
        )

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


# =========================
# 📌 LISTAR USUÁRIOS
# =========================
@router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioModel).all()


# =========================
# 📌 BUSCAR USUÁRIO POR ID
# =========================
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


# =========================
# 📌 DELETAR USUÁRIO
# =========================
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


# =========================
# 📌 ATUALIZAR USUÁRIO
# =========================
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

    # 🔎 Validação de e-mail único (exceto ele mesmo)
    if usuario.email:
        usuario_existente = get_usuario_por_email(db, usuario.email)

        if usuario_existente and usuario_existente.id != usuario_id:
            raise HTTPException(
                status_code=400,
                detail="E-mail já cadastrado"
            )

    # 🔄 Atualização dos campos
    usuario_db.nome = usuario.nome
    usuario_db.email = usuario.email
    usuario_db.idade = usuario.idade

    db.commit()
    db.refresh(usuario_db)

    return usuario_db
