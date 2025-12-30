from pydantic import BaseModel, EmailStr

class Usuario(BaseModel):
    nome: str
    email: EmailStr
    idade: int