# BFF - API de Receitas

Backend for Frontend que faz proxy para a API pública DummyJSON Recipes, adicionando autenticação por API Key.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Crie o arquivo `.env` na raiz do projeto:

```
API_KEY=minha-chave-secreta
```

## Rodar o servidor

```bash
.venv/bin/uvicorn bff.main:app --reload
```

Servidor disponível em http://127.0.0.1:8000
Documentação Swagger em http://127.0.0.1:8000/docs

## Autenticação

Todos os endpoints exigem o header `X-API-Key` com o valor definido no `.env`.

```bash
curl -H "X-API-Key: minha-chave-secreta" "http://127.0.0.1:8000/recipes/search?q=pasta"
```

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/recipes/search` | Busca receitas por termo (`q`, `limit`, `skip`) |
| GET | `/recipes/{recipe_id}` | Detalha uma receita pelo ID (1–50) |

## Estrutura

```
bff/
├── bff/
│   ├── __init__.py
│   └── main.py           # Aplicação FastAPI
├── .env                  # Variáveis de ambiente (não versionado)
├── requirements.txt
├── CLAUDE.md
└── claude_comandos.md    # Histórico de instruções do curso
```

## Regra: Registro de Instruções

Este projeto é um curso. A cada instrução recebida, o Claude deve adicionar uma entrada em `claude_comandos.md` com a data e uma descrição do que foi feito. Isso permite revisar o histórico de aprendizado no futuro.