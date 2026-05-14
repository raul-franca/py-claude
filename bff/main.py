# ─── Ponto de entrada da aplicação ─────────────────────────────────────────────
# [BÁSICO] main.py é o ponto de entrada do servidor. Sua única responsabilidade
# é criar o app FastAPI e registrar os módulos (rotas).
# Cada detalhe (auth, client, routes) vive no próprio módulo.

from fastapi import FastAPI

# [AVANÇADO] Importação relativa do router definido em routes.py.
from .routes import router

# [BÁSICO] Criamos a instância do FastAPI com metadados que aparecem na documentação
# automática disponível em /docs (Swagger UI) e /redoc.
app = FastAPI(
    title="API de Receitas (DummyJSON Proxy)",
    description="Busca e detalhamento de receitas usando a API DummyJSON como backend",
    version="1.0.0"
)

# [INTERMEDIÁRIO] include_router() registra todas as rotas do módulo routes.py no app.
# É aqui que o router "mini-app" se conecta ao app principal.
# Para adicionar novos grupos de rotas (ex: users, orders), basta criar outro router
# e incluí-lo aqui com um prefix diferente.
app.include_router(router)
