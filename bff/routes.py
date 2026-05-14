# ─── Rotas da API ──────────────────────────────────────────────────────────────
# [BÁSICO] Módulo responsável por definir todos os endpoints da API.
# Separar rotas do app principal (main.py) é uma boa prática: permite organizar
# endpoints por domínio e facilita adicionar novos grupos de rotas no futuro.

from fastapi import APIRouter, Depends, Query, Path

# [AVANÇADO] Importações relativas dos módulos do pacote.
# Cada módulo tem uma responsabilidade única (Single Responsibility Principle).
from .auth import get_api_key
from .client import dummyjson_get

# [INTERMEDIÁRIO] APIRouter é um "mini-app" do FastAPI.
# Agrupa rotas que podem ser incluídas no app principal via app.include_router().
# prefix="/recipes" aplica o prefixo automaticamente em todas as rotas deste router.
# tags=["recipes"] agrupa os endpoints na documentação Swagger (/docs).
router = APIRouter()


# ─── Healthcheck ───────────────────────────────────────────────────────────────
# [BÁSICO] @router.get() registra a rota no router, não diretamente no app.
# O app incluirá este router em main.py.
@router.get("/health", summary="Healthcheck", tags=["infra"])
async def health() -> dict[str, str]:
    """Retorna o status da aplicação. Usado para verificar se o servidor está no ar."""
    # [BÁSICO] Endpoints de healthcheck são convenção em APIs REST e microsserviços.
    # Orquestradores como Kubernetes usam esse endpoint para saber se o pod está saudável.
    return {"status": "ok"}


# ─── Receitas ──────────────────────────────────────────────────────────────────
@router.get(
    "/recipes/search",
    summary="Busca receitas por termo",
    tags=["recipes"],
    # [INTERMEDIÁRIO] dependencies=[Depends(get_api_key)] aplica a autenticação neste
    # endpoint sem precisar declarar o parâmetro na assinatura da função. O FastAPI
    # executa get_api_key antes de chamar search_recipes; se lançar HTTPException, a
    # execução para ali e o cliente recebe o erro.
    dependencies=[Depends(get_api_key)]
)
async def search_recipes(
    # [BÁSICO] Query(...) declara um parâmetro de query string obrigatório ('...' = required).
    # min_length=2 é uma validação automática feita pelo Pydantic antes de entrar na função.
    q: str = Query(..., min_length=2, description="Termo de busca"),
    # [BÁSICO] ge=1 (greater or equal) e le=50 (less or equal) definem o intervalo aceito.
    # Se o cliente enviar limit=0 ou limit=100, o FastAPI já rejeita com 422 Unprocessable Entity.
    limit: int = Query(10, ge=1, le=50, description="Resultados por página"),
    skip: int = Query(0, ge=0, description="Paginação: quantos pular")
) -> dict:
    """Busca receitas na API DummyJSON pelo termo informado, com suporte a paginação."""
    return await dummyjson_get(
        "/recipes/search",
        params={"q": q, "limit": limit, "skip": skip}
    )


@router.get(
    "/recipes/{recipe_id}",
    summary="Obtém detalhes de uma receita pelo ID",
    tags=["recipes"],
    dependencies=[Depends(get_api_key)]
)
async def get_recipe_by_id(
    # [BÁSICO] Path() declara e valida um parâmetro de path (parte da URL).
    # {recipe_id} na rota acima é preenchido com o valor recebido aqui.
    # ge=1 garante que IDs negativos ou zero sejam rejeitados automaticamente.
    recipe_id: int = Path(..., ge=1, description="ID da receita (1 a 50 na base DummyJSON)")
) -> dict:
    """Retorna os detalhes completos de uma receita pelo seu ID na base DummyJSON."""
    return await dummyjson_get(f"/recipes/{recipe_id}")
