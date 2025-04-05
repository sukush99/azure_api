from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Literal, Optional

class AzureConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="azure_conn.env", env_file_encoding="utf-8"
    )
    database_name: str
    server_name: str
    azure_sql_connection_string: str
    password_azure: str 
    username_azure: str

config = AzureConfig()