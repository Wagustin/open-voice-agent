import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Open Voice Agent"
    API_V1_STR: str = "/api/v1"
    WS_PATH: str = "/ws/voice"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "open-voice-agent-secret-key-change-me")
    API_KEY: str = os.getenv("VOICE_API_KEY", "kathy-voice-secure-token")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./voice_location_data.db")
    HERMES_AGENT_URL: str = os.getenv("HERMES_AGENT_URL", "http://localhost:8080")
    
    # Audio Settings
    SAMPLE_RATE: int = 16000
    CHANNELS: int = 1
    TTS_VOICE: str = "es-CO-SalomeNeural"
    TTS_PITCH: str = "-5Hz"
    
    # LLM & STT
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    STT_MODEL: str = "whisper-large-v3-turbo"

    class Config:
        env_file = ".env"

settings = Settings()
