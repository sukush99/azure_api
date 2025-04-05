from sqlalchemy.ext.declarative import declarative_base
from azure.identity import DefaultAzureCredential
from azure_config import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from loguru import logger
import urllib.parse

CONNECTION_STRING = (
        f"Driver={{ODBC Driver 18 for SQL Server}};"
        f"Server={config.server_name}.database.windows.net,1433;"
        f"Database={config.database_name};"
        f"UID={config.username_azure};"
        f"PWD={{{config.password_azure}}};"  # Enclose password in extra curly braces
        f"Encrypt=yes;"
        f"TrustServerCertificate=no"
    )

credential = DefaultAzureCredential()

params = urllib.parse.quote(CONNECTION_STRING)
CONNECTION_STRING_URL = "mssql+pyodbc:///?odbc_connect={0}".format(params)

try:
    # Create the database engine
    engine = create_engine(
        CONNECTION_STRING_URL, connect_args={"check_same_thread": False}
    )

    # Create a configured "Session" class
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Create a base class for declarative models
    Base = declarative_base()
    logger.info("Database connection established successfully.")
except Exception as e:
    logger.error(f"Error connecting to the database: {e}")
    raise