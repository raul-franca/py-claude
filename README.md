
# BFF para API de Receitas - FastAPI

Este é um Backend for Frontend (BFF) simples, de caráter educativo, que serve como camada de abstração para acessar a API pública de receitas [DummyJSON Recipes](https://dummyjson.com/docs/recipes). O objetivo deste projeto é fornecer um servidor em Python usando **FastAPI** que acessa a API de receitas externa e expõe esses dados de forma organizada para o frontend, com a implementação de autenticação via **chave de API**.

## Requisitos

- Python 3.12+
- FastAPI
- Uvicorn (para execução do servidor)
- httpx (para requisições HTTP assíncronas)
- python-dotenv (para carregar variáveis de ambiente de um arquivo `.env`)

## Instalação

1. **Crie um ambiente virtual:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure a chave de API:**

   Crie um arquivo `.env` na raiz do projeto:

   ```env
   API_KEY=SuaChaveSecretaAqui
   ```

## Como Executar

```bash
.venv/bin/uvicorn bff.main:app --reload
```

O servidor estará disponível em `http://127.0.0.1:8000`.
Documentação interativa (Swagger) em `http://127.0.0.1:8000/docs`.

## Autenticação

Todos os endpoints (exceto `/health`) exigem o header `X-API-Key`:

```bash
curl -H "X-API-Key: SuaChaveSecretaAqui" "http://127.0.0.1:8000/recipes/search?q=pasta"
```

## Endpoints

| Método | Rota | Auth | Descrição |
|--------|------|------|-----------|
| GET | `/health` | Não | Healthcheck — verifica se o servidor está no ar |
| GET | `/recipes/search` | Sim | Busca receitas por termo (`q`, `limit`, `skip`) |
| GET | `/recipes/{recipe_id}` | Sim | Detalha uma receita pelo ID (1–50) |

## Estrutura

```
bff/
├── bff/
│   ├── __init__.py
│   ├── client.py         # Cliente HTTP (dummyjson_get, timeout, erros)
│   ├── auth.py           # Autenticação por API Key (get_api_key)
│   ├── routes.py         # Endpoints (APIRouter)
│   └── main.py           # App FastAPI + include_router
├── .env                  # Variáveis de ambiente (não versionado)
├── requirements.txt
├── CLAUDE.md
└── claude_comandos.md    # Histórico de instruções do curso
```
