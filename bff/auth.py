# ─── Autenticação por API Key ───────────────────────────────────────────────────
# [BÁSICO] Módulo responsável exclusivamente pela autenticação da API.
# Centralizar auth aqui facilita trocar o mecanismo no futuro (ex: JWT, OAuth2)
# sem tocar nas rotas ou no cliente HTTP.

import os

from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

# [BÁSICO] load_dotenv() lê o arquivo .env e carrega as variáveis nele definidas
# como variáveis de ambiente. Sem isso, os.getenv() não encontraria API_KEY.
from dotenv import load_dotenv

load_dotenv()

# [BÁSICO] Nome do header HTTP que o cliente deve enviar com a chave.
# Ex: curl -H "X-API-Key: minha-chave" http://...
API_KEY_NAME = "X-API-Key"

# [INTERMEDIÁRIO] APIKeyHeader instrui o FastAPI a extrair o valor do header
# "X-API-Key" de cada requisição. auto_error=False significa que, se o header
# estiver ausente, o FastAPI não lança erro automaticamente — deixamos isso
# para a nossa função get_api_key tratar manualmente.
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# [BÁSICO] Lê a API_KEY definida no .env. Se não existir, retorna None.
# Em produção, essa variável viria de um cofre de segredos (ex: AWS Secrets Manager).
API_KEY = os.getenv("API_KEY")


# [INTERMEDIÁRIO] Depends(api_key_header) faz o FastAPI chamar api_key_header(request)
# automaticamente e injetar o resultado como argumento 'api_key' desta função.
# Esse padrão chama-se Dependency Injection e evita repetição de código em cada endpoint.
async def get_api_key(api_key: str = Depends(api_key_header)) -> str:
    """Valida a API Key recebida no header X-API-Key contra a variável de ambiente API_KEY."""
    # [BÁSICO] Se o header não veio ou o valor não bate com o esperado, nega o acesso.
    if api_key is None or api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Chave API inválida ou ausente. Use o header X-API-Key.",
            # [AVANÇADO] O header WWW-Authenticate informa ao cliente qual esquema
            # de autenticação é aceito. É um padrão da RFC 7235.
            headers={"WWW-Authenticate": "ApiKey"},
        )
    return api_key
