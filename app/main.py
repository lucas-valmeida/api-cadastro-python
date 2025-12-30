from fastapi import FastAPI
from app.routes.usuarios import router as usuarios_router

app = FastAPI(
    title="API de Cadastro",
    description="API simples para cadastro de usuários (FastAPI + Codespaces)",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "API funcionando via Codespaces"}

app.include_router(usuarios_router)
