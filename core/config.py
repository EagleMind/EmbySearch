from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MAIN_DB_URL: str
    CHROMA_PATH: str = "./chroma_data"
    WEBHOOK_SECRET: str 
    MASTER_API_KEY: str 
    model_config = {
        "env_file": ".env",
        "extra":"allow"
    }

    @classmethod
    def load(cls):
        return cls()

settings = Settings.load()