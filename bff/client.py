# ─── Cliente HTTP para a API DummyJSON ─────────────────────────────────────────
# [BÁSICO] Este módulo isola toda a lógica de comunicação com a API externa.
# Separar o cliente do servidor facilita testes, manutenção e troca de API.

# [INTERMEDIÁRIO] httpx é uma biblioteca HTTP moderna com suporte a async/await.
# Usamos ela no lugar de 'requests', pois 'requests' é síncrona e bloquearia
# o event loop do FastAPI.
import httpx

# [BÁSICO] FastAPI e status são importados aqui para lançar HTTPException
# diretamente do cliente, propagando erros HTTP ao chamador.
from fastapi import HTTPException, status

# [BÁSICO] Optional[X] é equivalente a dizer "pode ser X ou None".
from typing import Optional

# [AVANÇADO] URL base da API externa centralizada como constante.
# Facilita trocar o backend sem alterar os endpoints.
DUMMYJSON_BASE_URL = "https://dummyjson.com"


async def dummyjson_get(endpoint: str, params: Optional[dict[str, str | int]] = None) -> dict:
    """Realiza uma requisição GET à API DummyJSON e retorna o JSON da resposta.

    Args:
        endpoint: Caminho do endpoint (ex: '/recipes/search').
        params: Parâmetros de query string opcionais.

    Raises:
        HTTPException: 4xx/5xx se a API retornar erro, 502 em falha de conexão, 500 em erro inesperado.
    """
    # [BÁSICO] f-string monta a URL completa concatenando a base com o endpoint recebido.
    url = f"{DUMMYJSON_BASE_URL}{endpoint}"

    # [INTERMEDIÁRIO] Define um timeout de 10 segundos para a requisição.
    # Sem timeout, uma API lenta travaria a requisição indefinidamente.
    timeout = httpx.Timeout(10.0)

    # [INTERMEDIÁRIO] 'async with' é um context manager assíncrono. Garante que o
    # cliente HTTP seja fechado corretamente ao final do bloco, mesmo se ocorrer erro.
    # Criar o client aqui (por requisição) é simples, mas em produção o ideal é
    # reutilizar um único client via lifespan para melhor performance.
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            # [INTERMEDIÁRIO] 'await' suspende esta corrotina até a resposta chegar,
            # liberando o event loop para processar outras requisições enquanto espera.
            # Isso é a base do modelo assíncrono: I/O não bloqueia o servidor.
            response = await client.get(url, params=params)

            # [BÁSICO] raise_for_status() lança uma exceção se o status code for 4xx ou 5xx.
            response.raise_for_status()

            # [BÁSICO] .json() desserializa o corpo da resposta de JSON para dict Python.
            return response.json()

        except httpx.HTTPStatusError as exc:
            # [INTERMEDIÁRIO] Captura erros HTTP (4xx/5xx) da API externa e os repropaga
            # como HTTPException para o cliente do nosso BFF. Preservamos o status code
            # original para transparência.
            raise HTTPException(
                status_code=exc.response.status_code,
                detail=f"Erro na API DummyJSON: {exc.response.text}"
            )
        except httpx.RequestError as exc:
            # [INTERMEDIÁRIO] Captura falhas de rede: DNS não resolvido, timeout,
            # conexão recusada, etc. Mapeamos para 502 Bad Gateway, que semanticamente
            # significa "o servidor upstream não respondeu corretamente".
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail=f"Erro de conexão com DummyJSON: {str(exc)}"
            )
        except Exception as exc:
            # [BÁSICO] Captura qualquer outro erro inesperado para evitar que o servidor
            # retorne um traceback Python exposto ao cliente.
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro interno: {str(exc)}")
