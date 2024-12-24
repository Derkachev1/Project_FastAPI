from pydantic_settings import BaseSettings

class RunConfig(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000

class ApiPrefix(BaseSettings):
    prefix: str = "/api"

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()

settings = Settings()
