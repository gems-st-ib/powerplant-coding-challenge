
FROM python:3.12-slim

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev --no-interaction --no-ansi

COPY app ./app

EXPOSE 8888

ENTRYPOINT ["poetry", "run", "uvicorn", "app.app.main:app", "--host", "0.0.0.0", "--port", "8888"]
