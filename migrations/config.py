import os

SERVICE_NAME = os.environ.get('SERVICE_NAME', 'Migrations')
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
LOG_FORMAT = os.environ.get('LOG_FORMAT', f'[%(levelname)s] service={SERVICE_NAME} message=%(name)s - %(message)s')
'''
Log level options:
- 'CRITICAL'
- 'FATAL'
- 'ERROR'
- 'WARN'
- 'WARNING'
- 'INFO'
- 'DEBUG'
- 'NOTSET'
'''

# Database Settings
DATABASE_CONNECTION_STRING = os.environ.get('DATABASE_CONNECTION_STRING', f'postgresql://admin:admin@localhost:5433/postgres')
DATABASE_ALEMBIC_INI_FILE = os.environ.get('DATABASE_ALEMBIC_INI_FILE', './alembic.ini')
DATABASE_DEFAULT_SCHEMA = os.environ.get('DATABASE_SCHEMA', 'public')
DATABASE_TENANT_SCHEMAS = os.environ.get('DATABASE_TENANT_SCHEMAS', 'tenant1,tenant2,tenant3').split(',')
