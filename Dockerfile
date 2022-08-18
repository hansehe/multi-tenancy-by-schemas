FROM python:3.9-slim as dev

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM dev as final

COPY ./alembic.ini ./alembic.ini
COPY ./migrate.py ./migrate.py
COPY ./migrations ./migrations

ENV DATABASE_CONNECTION_STRING=postgresql://admin:admin@postgres-db:5432/postgres

ENTRYPOINT python migrate.py