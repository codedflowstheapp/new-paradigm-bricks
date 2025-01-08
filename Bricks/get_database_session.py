from coded_flows.types import PostgresDsn, Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


coded_flows_metadata = {
    "display_name": "PG Session",
    "description": "Postgres Session.",
    "icon": "database",
}


def get_database_session(postgres_dsn: PostgresDsn) -> Any:
    # Create a SQLAlchemy engine using the provided DSN
    engine = create_engine(postgres_dsn)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
