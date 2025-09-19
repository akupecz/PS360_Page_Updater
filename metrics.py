import sqlalchemy as sa
from sqlalchemy import text
from config import DB_SECRET_HOST, DB_SECRET_LOGIN
import citygeo_secrets as cgs

def connect_to_target(creds: dict, test: bool) -> sa.Engine: 
    db_creds = creds[DB_SECRET_HOST]
    creds_schema = creds[DB_SECRET_LOGIN]
    url_object = sa.URL.create(
        drivername='postgresql+psycopg',
        username=creds_schema['login'],
        password=creds_schema['password'],
        host=db_creds['host'],
        port=db_creds['port'],
        database=db_creds['database']
    )
    engine = sa.create_engine(url_object)
    engine.connect()
    return engine