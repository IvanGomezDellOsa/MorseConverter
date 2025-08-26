# Python 3.13-slim para menor tamaño de imagen
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Flask (por defecto 5000)
EXPOSE 5000

# docker-compose up --build // http://localhost:5000
CMD ["python", "app.py"]