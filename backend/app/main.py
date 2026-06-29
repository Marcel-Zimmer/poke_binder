from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Inicializa o app FastAPI
app = FastAPI(
    title="HoloDex API",
    description="Backend para gerenciamento de coleção de TCG",
    version="1.0.0"
)

# Configuração de CORS (Permite que o Angular no localhost converse com o FastAPI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Em produção, mudamos para o domínio do seu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota raiz simples para testar
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do HoloDex! O servidor está rodando perfeitamente."}

# Uma rota simulando o futuro
@app.get("/api/ping")
def ping():
    return {"status": "ok", "db_connected": False}
