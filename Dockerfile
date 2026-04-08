FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

# Dependências do sistema (Playwright precisa de libs)
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    gnupg \
    unzip \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Diretório de trabalho
WORKDIR /app

# Copia requirements.txt primeiro (melhor para cache)
COPY requirements.txt .

# INSTALA TODAS AS DEPENDÊNCIAS do requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do projeto
COPY . .

# Instala Playwright
RUN pip install playwright \
    && python -m playwright install chromium --with-deps

# Garante que a pasta data/ existe
RUN mkdir -p /app/data

# Comando padrão
CMD ["python", "app/main.py"]