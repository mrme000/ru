from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from typing import Optional

# Load .env file
load_dotenv()

class Settings(BaseSettings):
    # AWS Configuration
    aws_access_key_id: Optional[str] = None
    aws_secret_access_key: Optional[str] = None
    aws_region: str = "us-east-1"
    
    # DynamoDB
    dynamodb_table_name: Optional[str] = None
    
    # AWS Cognito
    cognito_user_pool_id: Optional[str] = None
    cognito_client_id: Optional[str] = None
    cognito_client_secret: Optional[str] = None
    
    # API Keys for AI Services
    groq_api_key: Optional[str] = None
    huggingface_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None  # Legacy, keeping for backward compatibility
    replicate_api_key: Optional[str] = None  # Legacy, keeping for backward compatibility
    deepai_api_key: Optional[str] = None  # Legacy, keeping for backward compatibility
    
    # Application Settings
    app_name: str = "RU Carpooling Backend"
    log_level: str = "INFO"
    debug: bool = False
    
    # JWT Configuration
    jwt_secret_key: str = "99ySHm25hfxUQI3MaSA3vKQcbHL1nCOzcEIdojc5"  # Change this in production!
    jwt_algorithm: str = "HS256"
    jwt_expiration_minutes: int = 30
    
    # S3 Configuration
    s3_bucket_name: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

settings = Settings()
