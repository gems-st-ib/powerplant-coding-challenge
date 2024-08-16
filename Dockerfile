# Usa una imagen base de Python 3.12
FROM python:3.12-slim

# Instala Poetry
RUN pip install poetry

WORKDIR /app

COPY . .

RUN poetry install

ENTRYPOINT ["poetry", "run", "uvicorn", "app.app.main:app", "--host", "0.0.0.0", "--port", "8888"]
