from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False
    tapis_base_url: str
    sandbox_server_url: str
    mongodb_uri: str
    class Config:
        env_file: str = ".env"
        extra = "ignore"

app_settings = AppSettings()