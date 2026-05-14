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

**Iniciar:**
```bash
.venv/bin/uvicorn bff.main:app --reload
```

Servidor disponível em http://127.0.0.1:8000
Documentação Swagger em http://127.0.0.1:8000/docs

**Parar:**
```bash
pkill -f "uvicorn bff.main:app"
```

**Reload manual** (parar e reiniciar):
```bash
pkill -f "uvicorn bff.main:app" && .venv/bin/uvicorn bff.main:app --reload
```

> Com `--reload` ativo, o uvicorn já recarrega automaticamente ao detectar mudanças em arquivos `.py`.

## Autenticação

Todos os endpoints exigem o header `X-API-Key` com o valor definido no `.env`.

```bash
curl -H "X-API-Key: minha-chave-secreta" "http://127.0.0.1:8000/recipes/search?q=pasta"
```

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/health` | Healthcheck — verifica se o servidor está no ar (sem autenticação) |
| GET | `/recipes/search` | Busca receitas por termo (`q`, `limit`, `skip`) |
| GET | `/recipes/{recipe_id}` | Detalha uma receita pelo ID (1–50) |

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

## Regras

- **Registro de instruções:** A cada instrução recebida, adicionar uma entrada em `claude_comandos.md` com a data e descrição do que foi feito.
- **Atualizar CLAUDE.md:** Sempre que a estrutura, endpoints ou comportamento do projeto mudar, atualizar este arquivo para refletir o estado atual.
- **Atualizar README.md:** Sempre que a estrutura, endpoints, comando de execução ou comportamento do projeto mudar, atualizar o `README.md` para refletir o estado atual.