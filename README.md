# 📌 API de Cadastro de Usuários --- FastAPI

API REST simples desenvolvida em **Python com FastAPI**, com foco em
boas práticas de backend, organização de código e validação de dados.

Projeto criado como parte do meu **portfólio de desenvolvedor**, com o
objetivo de demonstrar lógica de programação, estruturação de APIs e
entendimento do fluxo backend.

------------------------------------------------------------------------

## 🚀 Tecnologias Utilizadas

-   Python 3
-   FastAPI
-   Uvicorn
-   Pydantic
-   Swagger (OpenAPI)

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

### 🔹 GET `/`

Endpoint de teste para verificar se a API está funcionando.

Resposta: { "message": "API funcionando via Codespaces" }

------------------------------------------------------------------------

### 🔹 POST `/usuarios`

Cria um novo usuário com validação de dados.

Body (JSON): { "nome": "Lucas", "email": "lucas@email.com", "idade": 25
}

Resposta: { "mensagem": "Usuário criado com sucesso", "usuario": {
"nome": "Lucas", "email": "lucas@email.com", "idade": 25 } }

------------------------------------------------------------------------

## 📄 Documentação (Swagger)

Após iniciar a aplicação, a documentação interativa pode ser acessada
em:

/docs

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

-   Persistência de dados (SQLite ou PostgreSQL)
-   CRUD completo de usuários
-   Validações de negócio
-   Autenticação
-   Testes automatizados

------------------------------------------------------------------------

## 👨‍💻 Autor

Desenvolvido por **Lucas Vieira**
