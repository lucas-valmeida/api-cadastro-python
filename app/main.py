from fastapi import FastAPI
from app.routes.usuarios import router as usuarios_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Cadastro",
    description="API com persistência em SQLite",
    version="1.1.0"
)

@app.get("/")
def read_root():
    return {"message": "API funcionando com SQLite"}

app.include_router(usuarios_router)
