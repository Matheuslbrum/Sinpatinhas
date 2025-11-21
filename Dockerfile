FROM python:3.11-slim

# Instalar dependências do GeoDjango
RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    libgeos-dev \
    libproj-dev \
    proj-bin \
    proj-data \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o projeto
COPY . .

# Expor porta 8000
EXPOSE 8000

# Comando de execução
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:${PORT}"]
