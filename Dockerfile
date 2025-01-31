# Usar uma imagem oficial do Python 3.12 como base
FROM python:3.12-slim

# Atualizar o sistema e instalar ffmpeg
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar os arquivos do projeto para o contêiner
COPY . /app

# Instalar as dependências do projeto
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expor a porta 8000 para o serviço
EXPOSE 8000

# Definir a variável de ambiente para produção
ENV PYTHONUNBUFFERED=1

# Comando para iniciar o aplicativo FastAPI usando Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
