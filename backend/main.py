import json
from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from database import init_db
from audio_pipeline import pipeline
from routes import location

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(location.router, prefix=settings.API_V1_STR)

@app.get("/health")
async def health_check():
    return {
        "status": "online",
        "service": "open-voice-agent",
        "tts_voice": settings.TTS_VOICE,
        "location_tracking": "enabled"
    }

@app.websocket("/ws/voice")
async def websocket_voice_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text(json.dumps({"type": "session_start", "message": "Voice & Spatial pipeline ready"}))
    
    try:
        while True:
            data = await websocket.receive()
            if "text" in data:
                payload = json.loads(data["text"])
                if payload.get("type") == "user_transcript":
                    text = payload.get("text", "")
                    
                    # 1. State: processing
                    await websocket.send_text(json.dumps({"type": "state", "state": "processing"}))
                    
                    # 2. Get LLM response from Kathy / Hermes Agent
                    response_text = await pipeline.query_hermes_agent(text)
                    await websocket.send_text(json.dumps({
                        "type": "agent_response_text",
                        "text": response_text
                    }))
                    
                    # 3. Synthesize Salomé voice audio
                    audio_bytes = await pipeline.process_text_to_speech(response_text)
                    
                    # 4. Stream audio binary to client
                    await websocket.send_text(json.dumps({"type": "state", "state": "speaking"}))
                    await websocket.send_bytes(audio_bytes)
                    await websocket.send_text(json.dumps({"type": "state", "state": "idle"}))

            elif "bytes" in data:
                # Incoming audio chunk (PCM/Opus) for streaming STT
                pass

    except WebSocketDisconnect:
        print("Voice client disconnected.")
