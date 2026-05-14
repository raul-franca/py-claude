# Histórico de Instruções

Registro de todas as instruções passadas ao Claude neste projeto.

---

## 2026-05-14

1. **"analiza o esse projeto"** — Exploração e análise completa do projeto: estrutura, tecnologias, endpoints, dependências, padrões arquiteturais e pontos de melhoria.

2. **"crie um venv para rodar o projeto"** — Criação do ambiente virtual `.venv` e instalação das dependências via `pip install -r requirements.txt`.

3. **"rode o projeto"** — Identificou ausência do `.env`, solicitou a chave e iniciou o servidor com `uvicorn bff.main:app --reload`.

4. **"crei o .env"** — Criação do arquivo `.env` com `API_KEY=minha-chave-secreta` e reinício do servidor.

5. **Correção do erro 401** — Adicionado `load_dotenv()` em `bff/main.py` pois o `.env` não estava sendo carregado automaticamente.

6. **"crie um claude.md"** — Criação do `CLAUDE.md` com documentação do projeto: setup, como rodar, autenticação, endpoints e estrutura de arquivos.

7. **"commit isso"** — Commit de `bff/main.py` e `CLAUDE.md`.

8. **"push isso"** — Push para `raul-franca/py-claude` na branch `main`.

9. **"Crie um claude_comandos.md e add todas as instruções que eu passar no arquivo claude.md add essa regra tbm pois esse projeto é um curso e eu vou querer revisar o que eu fiz no futuro"** — Criação deste arquivo e adição da regra no `CLAUDE.md`.

10. **"add um endpoint de healthcheck"** — Adicionado endpoint `GET /health` em `bff/main.py` que retorna `{"status": "ok"}`, sem autenticação.

11. **"@bff/main.py add docstring para as funcoes"** — Adicionadas docstrings em todas as funções de `bff/main.py`: `get_api_key`, `dummyjson_get`, `health`, `search_recipes` e `get_recipe_by_id`.