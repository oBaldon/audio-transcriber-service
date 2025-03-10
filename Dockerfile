# Base oficial com Python 3.10 (ou 3.12 se preferir)
FROM python:3.10-slim

# Definir variável de ambiente para evitar prompt durante instalação
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Copiar apenas o necessário primeiro (melhora cache de build)
COPY requirements.txt .

# Instalar dependências do sistema + pip
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
 && pip install --upgrade pip \
 && pip install -r requirements.txt \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Copiar o restante dos arquivos do projeto
COPY . .

# Expor a porta padrão da aplicação
EXPOSE 8000

# Comando padrão para iniciar o servidor FastAPI com Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
