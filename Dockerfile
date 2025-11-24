FROM python:3.11-slim

# Instalar dependências de sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Diretório da aplicação
WORKDIR /app

# Instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar projeto
COPY . .

# Expor porta
EXPOSE 8000

# Rodar migrações + coletar estáticos + iniciar Gunicorn
CMD ["sh", "-c", "\
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    gunicorn core.wsgi:application --bind 0.0.0.0:${PORT:-8000} \
"]
