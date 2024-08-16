# Usa una imagen base de Python 3.12
FROM python:3.12-slim

# Establece el directorio de trabajo
#WORKDIR /app

# Copia los archivos de tu proyecto
COPY pyproject.toml poetry.lock ./

# Instala Poetry
RUN pip install poetry

# Instala las dependencias del proyecto
RUN poetry install

# Copia el resto del código fuente
COPY ./app /app

# Expone el puerto en el que tu aplicación escuchará
EXPOSE 8888

RUN poetry shell

# Define el comando por defecto para ejecutar la aplicación
#CMD ["poetry", "run", "uvicorn", "app.app.main:app", "--host", "127.0.0.1", "--port", "8888"]
CMD ["uvicorn", "app.app.main:app", "--host", "127.0.0.1", "--port", "8888"]

