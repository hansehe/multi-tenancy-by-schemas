import logging
from typing import List

import sqlalchemy
from alembic import command, script
from alembic.config import Config
from alembic.runtime import migration

from migrations import config

logging.basicConfig(format=config.LOG_FORMAT, level=config.LOG_LEVEL)
log = logging.getLogger(__name__)


def RunMigrations(connectionString: str = config.DATABASE_CONNECTION_STRING,
                  schemas: List[str] = config.DATABASE_TENANT_SCHEMAS,
                  scriptLocation: str = 'migrations',
                  alembicFile: str = 'alembic.ini') -> None:
    for schema in schemas:
        log.info(f'Running DB migrations in {scriptLocation} on schema {schema}')
        alembicCfg = GetAlembicConfig(connectionString=connectionString,
                                      schema=schema,
                                      scriptLocation=scriptLocation,
                                      alembicFile=alembicFile)
        command.upgrade(alembicCfg, 'head')


def CheckPendingMigrations(connectionString: str = config.DATABASE_CONNECTION_STRING,
                           schema: str = config.DATABASE_DEFAULT_SCHEMA,
                           scriptLocation: str = 'DocumentStore/migrations',
                           alembicFile: str = 'alembic.ini') -> bool:
    alembicCfg = GetAlembicConfig(connectionString=connectionString,
                                  schema=schema,
                                  scriptLocation=scriptLocation,
                                  alembicFile=alembicFile)
    script_ = script.ScriptDirectory.from_config(alembicCfg)
    engine = sqlalchemy.create_engine(connectionString)
    with engine.begin() as connection:
        connection.execution_options(schema_translate_map={None: schema})
        context = migration.MigrationContext.configure(connection,
                                                       opts={
                                                           'version_table_schema': schema,
                                                           'include_schemas': True
                                                       })
        return context.get_current_revision() != script_.get_current_head()


def GetAlembicConfig(connectionString: str = config.DATABASE_CONNECTION_STRING,
                     schema: str = config.DATABASE_DEFAULT_SCHEMA,
                     scriptLocation: str = 'DocumentStore/migrations',
                     alembicFile: str = 'alembic.ini'):
    alembicCfg = Config(file_=alembicFile)
    alembicCfg.set_main_option('script_location', scriptLocation)
    alembicCfg.set_main_option('sqlalchemy.url', connectionString)
    alembicCfg.set_main_option('database.schema', schema)
    return alembicCfg


if __name__ == "__main__":
    RunMigrations(scriptLocation='./migrations', alembicFile='../alembic.ini')
