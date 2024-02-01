# Usa la imagen de Python 3 en Alpine
FROM python:3-alpine

# Instala las dependencias de compilación
RUN apk add --no-cache musl-dev gcc

# Establece el directorio de trabajo
WORKDIR /app

# Copia todos los archivos al directorio de trabajo
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["python", "-u", "main.py"]