FROM python:3.10-slim-buster


ENV API_V1_PREFIX="/api/v1" \
  DEBUG=True \
  PROJECT_NAME="Heroes App (local)" \
  VERSION="0.1.0" \
  DESCRIPTION="The API for Heroes app." \
  POSTGRES_USERNAME="postgres" \
  POSTGRES_PASSWORD="thepass123" \
  POSTGRES_HOST='172.17.0.2' \
  POSTGRES_PORT="5432" \
  POSTGRES_DATABASE="postgres" \
  DB_EXCLUDE_TABLES="[]" \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.13

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /vyce-backend
COPY poetry.lock pyproject.toml /vyce-backend/


# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /vyce-backend

RUN chmod a+x /vyce-backend/docker-env-entrypoint

ENTRYPOINT [ "/vyce-backend/docker-env-entrypoint" ]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
