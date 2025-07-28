FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir efficientnet_pytorch

# Copiar código de la aplicación
COPY . .

# Crear directorios necesarios
RUN mkdir -p modelo
RUN mkdir -p images

# Exponer puerto
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD exec uvicorn main:app --host 0.0.0.0 --port 8080