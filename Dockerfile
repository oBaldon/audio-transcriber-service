# Base oficial com Python 3.10 (ou altere para 3.12 se preferir)
FROM python:3.10-slim

# Setar diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto para dentro do container
COPY . .

# Atualizar pip e instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Instalar as dependências do Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expor a porta padrão da aplicação
EXPOSE 8000

# Comando para iniciar o servidor FastAPI com Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
