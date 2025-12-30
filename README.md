# 📌 API de Cadastro de Usuários --- FastAPI

API REST desenvolvida em **Python com FastAPI**, utilizando **SQLite e 
SQLAlchemy** para persistência de dados, com CRUD completo de usuários.

Projeto criado como parte do meu **portfólio de desenvolvedor**, 
com foco em boas práticas de backend, organização de código e regras 
de negócio.

------------------------------------------------------------------------

## 🚀 Tecnologias Utilizadas

-   Python 3
-   FastAPI
-   Uvicorn
-   Pydantic
-   Swagger (OpenAPI)
-   SQLAlchemy
-   SQLite

------------------------------------------------------------------------

## 🧠 Conceitos Aplicados

-   Criação de API REST
-   Validação automática de dados com Pydantic
-   Organização de projeto em módulos
-   Uso de APIRouter
-   Documentação automática com Swagger
-   Execução em ambiente cloud (GitHub Codespaces)

------------------------------------------------------------------------

## 📁 Estrutura do Projeto

app/ ├── main.py ├── routes/ │ └── usuarios.py ├── schemas/ │ └──
usuario.py requirements.txt README.md

------------------------------------------------------------------------

## 🔗 Endpoints Disponíveis

- GET `/` → Verificação da API
- POST `/usuarios` → Criar usuário
- GET `/usuarios` → Listar usuários
- GET `/usuarios/{id}` → Buscar usuário por ID
- PUT `/usuarios/{id}` → Atualizar usuário
- DELETE `/usuarios/{id}` → Deletar usuário
------------------------------------------------------------------------

## ▶️ Como Executar o Projeto

1.  Clonar o repositório git clone
    https://github.com/lucas-valmeida/api-cadastro-python.git

2.  Criar ambiente virtual python -m venv venv

3.  Ativar o ambiente virtual

Windows: venv`\Scripts`{=tex}`\activate`{=tex}

Linux / macOS: source venv/bin/activate

4.  Instalar dependências pip install -r requirements.txt

5.  Executar o servidor uvicorn app.main:app --host 0.0.0.0 --port 8000
    --reload

------------------------------------------------------------------------

## 🎯 Próximas Melhorias Planejadas

- Validação de email único
- Paginação de resultados
- Autenticação (JWT)
- Testes automatizados
- Dockerização da aplicação

------------------------------------------------------------------------

## 👨‍💻 Autor

Desenvolvido por **Lucas Vieira**
