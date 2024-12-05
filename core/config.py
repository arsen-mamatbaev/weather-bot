from pydantic import Field
from pydantic_settings import BaseSettings


class BotSettings(BaseSettings):
    token: str = Field(alias='BOT_TOKEN')
    
    
class PostgresSettings(BaseSettings):
    host: str = Field(alias='POSTGRES_HOST')
    port: int = Field(alias='POSTGRES_PORT')
    user: str = Field(alias='POSTGRES_USER')
    password: str = Field(alias='POSTGRES_PASSWORD')
    
    
class RedisSettings(BaseSettings):
    host: str = Field(alias='REDIS_HOST')
    port: int = Field(alias='REDIS_PORT')
    

class DatabaseSettings(BaseSettings):
    postgres: PostgresSettings = PostgresSettings()
    redis: RedisSettings = RedisSettings()
    
    
class OpenWeatherMapSettings(BaseSettings):
    token: str = Field(alias='OPENWEATHERMAP_TOKEN')
    
    
class Settings(BaseSettings):
    project_name: str = Field(alias='PROJECT_NAME')
    project_version: str = Field(alias='PROJECT_VERSION')
    
    bot: BotSettings = BotSettings()
    database: DatabaseSettings = DatabaseSettings()
    openweathermap: OpenWeatherMapSettings = OpenWeatherMapSettings()
    
    debug: bool = Field(alias='DEBUG')


settings = Settings()
