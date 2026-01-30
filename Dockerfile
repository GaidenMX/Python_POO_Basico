# --- Stage 1: Builder ---
FROM python:3.11-slim as builder

WORKDIR /build

# Evitar archivos .pyc y caché de pip para reducir peso
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependencias de compilación si fueran necesarias (ej: gcc, libpq)
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt


# --- Stage 2: Final (Producción) ---
FROM python:3.11-slim-bookworm

WORKDIR /app

# Crear un usuario no-root por seguridad
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copiar solo las librerías instaladas desde el builder
COPY --from=builder /root/.local /home/appuser/.local
# Copiar solo el código fuente necesario (excluyendo tests y docs)
COPY ./src ./src

# Configurar variables de entorno
ENV PATH=/home/appuser/.local/bin:$PATH
ENV PYTHONPATH=/app/src
ENV PYTHONDONTWRITEBYTECODE=1

# Cambiar al usuario limitado
USER appuser

# Comando de ejecución
CMD ["python", "src/main.py"]