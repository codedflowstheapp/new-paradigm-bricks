from coded_flows.types import PostgresDsn, Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


coded_flows_metadata = {
    "display_name": "PG Session",
    "description": "Postgres Session.",
    "icon": "database",
    "docker": {
        "service": "db-postgres",
        "image": "postgres",
        "image-version": 16,
        "ports": [{"target": 5432, "published": 5432, "protocol": "tcp"}],
        "volumes": [{"name": "db-volume", "container-path": "/data"}],
        "networks": ["backend"],
        "secrets": [{"name": "postgres_password", "env": "POSTGRES_PASSWORD_FILE"}],
    },
}


def get_database_session(postgres_dsn: PostgresDsn) -> Any:
    # Create a SQLAlchemy engine using the provided DSN
    engine = create_engine(postgres_dsn)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
