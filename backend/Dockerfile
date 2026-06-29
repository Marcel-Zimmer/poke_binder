FROM python:3.13-slim

WORKDIR /app

# Impede o Python de gerar arquivos .pyc e força o log a aparecer no terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala as dependências do sistema necessárias para o PostgreSQL (psycopg2)
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copia apenas o arquivo de dependências primeiro (melhora o cache do Docker)
COPY requirements.txt .

# Instala as bibliotecas
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código
COPY . .

# Comando padrão (será sobrescrito pelo docker-compose no ambiente de desenvolvimento)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
