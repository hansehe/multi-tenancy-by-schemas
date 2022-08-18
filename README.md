# Multi Tenancy By Schemas
Concept on multi tenancy separated by schemas.


## Build, Test And Run With Docker
```bash
# https://github.com/hansehe/DockerBuildManagement
pip install --upgrade DockerBuildManagement
dbm -swarm -start
dbm -test
dbm -swarm -stop
```

## Development outside of container
```bash
pip install -r requirements.txt
python migrate.py
```

Note! If installation fails with psycopg2-binary on windows, then manually download the wheel package from:
- https://www.lfd.uci.edu/~gohlke/pythonlibs/#psycopg

And install with pip:
- pip install psycopg2-2.8.6-cp39-cp39-win_amd64

## Alembic - Generic single-database configuration.
### Links & Tips
- https://alembic.sqlalchemy.org/en/latest/
- https://www.compose.com/articles/schema-migrations-with-alembic-python-and-postgresql/

### Add Revision Script
```
alembic revision -m "<revision_name>"
```

### Add Revision Scripts Based On Models
```
alembic revision --autogenerate -m "<revision_name>"
```

### Run Migration
```
alembic upgrade head
```
