# ── FILE: backend/Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY ./pyproject.toml ./poetry.lock* /app/
RUN pip install --no-cache-dir poetry && poetry config virtualenvs.create false && \
poetry install --no-interaction --no-ansi
COPY . /app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


# ── FILE: backend/pyproject.toml
[tool.poetry]
name = "mujadadi-api"
version = "0.1.0"
description = "Mujadadi API (FastAPI)"
authors = ["Mujadadi Group <team@mujadadi.com>"]
[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.115.0"
uvicorn = "^0.30.0"
pydantic-settings = "^2.5.2"
sqlalchemy = "^2.0.35"
sqlmodel = "^0.0.24"
python-multipart = "^0.0.9"


[tool.poetry.group.dev.dependencies]
httpx = "^0.27.0"
pytest = "^8.0.0"