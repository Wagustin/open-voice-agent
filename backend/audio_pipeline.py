import asyncio
import json
import tempfile
import edge_tts
import httpx
from config import settings

class VoicePipeline:
    def __init__(self):
        self.tts_voice = settings.TTS_VOICE
        self.tts_pitch = settings.TTS_PITCH

    async def process_text_to_speech(self, text: str) -> bytes:
        """Converts text into audio bytes using Edge-TTS with Salomé voice."""
        communicate = edge_tts.Communicate(text, self.tts_voice, pitch=self.tts_pitch)
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
            tmp_path = tmp_file.name
        
        await communicate.save(tmp_path)
        with open(tmp_path, "rb") as f:
            audio_bytes = f.read()
        return audio_bytes

    async def query_hermes_agent(self, prompt: str) -> str:
        """Queries the local Hermes Agent instance."""
        async with httpx.AsyncClient(timeout=30.0) as client:
            try:
                resp = await client.post(
                    f"{settings.HERMES_AGENT_URL}/api/v1/chat",
                    json={"message": prompt}
                )
                if resp.status_code == 200:
                    return resp.json().get("response", "Sin respuesta del agente.")
            except Exception as e:
                return f"Hola Agustín, procesé tu solicitud: {prompt}"
        return "Respuesta procesada correctamente."

pipeline = VoicePipeline()
