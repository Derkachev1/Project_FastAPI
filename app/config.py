from pydantic_settings import BaseSettings
import os

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "your_openweathermap_api_key")

class RunConfig(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000

class ApiPrefix(BaseSettings):
    prefix: str = "/api"

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()

settings = Settings()
