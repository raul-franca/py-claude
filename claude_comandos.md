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

12. **"add type hints nas funções"** — Adicionados type hints de retorno em todas as funções de `bff/main.py`. Também tipado o parâmetro `params` de `dummyjson_get` como `dict[str, str | int]`.

13. **"add comentarios detalhados do basico ao avancado add no claude"** — Adicionados comentários educacionais detalhados em todo o `bff/main.py`, categorizados por nível `[BÁSICO]`, `[INTERMEDIÁRIO]` e `[AVANÇADO]`. Cobrem: imports, FastAPI, async/await, Depends, Query/Path, HTTPException, timeouts, context managers e padrões REST.

14. **"separe o codigo em cliente e servidor"** — Código separado em dois módulos: `bff/client.py` (lógica HTTP com DummyJSON: `dummyjson_get`, timeout, tratamento de erros) e `bff/main.py` (app FastAPI, autenticação, endpoints). O `main.py` importa o cliente via importação relativa `from .client import dummyjson_get`, desacoplando transporte de roteamento.

15. **"seria melhor com um arquivo para auth e rotas tbm"** — Separação completa em 4 módulos: `client.py` (HTTP), `auth.py` (API Key, `get_api_key`), `routes.py` (endpoints via `APIRouter`, tags Swagger), `main.py` (só cria o app e registra o router via `app.include_router()`). Cada arquivo tem uma única responsabilidade (Single Responsibility Principle).

16. **"sempre atualize o @CLAUDE.md"** — Adicionada regra no `CLAUDE.md`: sempre atualizar o arquivo quando estrutura, endpoints ou comportamento do projeto mudar. Estrutura e tabela de endpoints também atualizadas para refletir o estado atual (4 módulos + endpoint `/health`).

17. **"sempre atualizar o @README.md"** — Adicionada regra no `CLAUDE.md`: sempre atualizar `README.md` quando estrutura, endpoints ou comportamento mudar. `README.md` atualizado: comando de execução corrigido (era `dotenv run fastapi dev bff/main.py`, agora `.venv/bin/uvicorn bff.main:app --reload`), tabela de endpoints com coluna Auth, estrutura de 4 módulos e seção de autenticação.

18. **"passe a fazer os commits em portugues"** — Preferência registrada: todas as mensagens de commit deste projeto devem ser escritas em português.

19. **"add comandos para parar a aplicação e para fazer reload"** — Adicionados no `README.md` e `CLAUDE.md`: comando para parar (`pkill -f "uvicorn bff.main:app"`), nota sobre reload automático via `--reload`, e comando para reload manual (pkill + reinício).