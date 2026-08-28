import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from audio_pipeline import pipeline

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {
        "status": "online",
        "service": "open-voice-agent",
        "tts_voice": settings.TTS_VOICE
    }

@app.websocket("/ws/voice")
async def websocket_voice_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text(json.dumps({"type": "session_start", "message": "Voice pipeline ready"}))
    
    try:
        while True:
            data = await websocket.receive()
            if "text" in data:
                # Text input or STT payload received
                payload = json.loads(data["text"])
                if payload.get("type") == "user_transcript":
                    text = payload.get("text", "")
                    
                    # 1. Notify client LLM is thinking
                    await websocket.send_text(json.dumps({"type": "state", "state": "processing"}))
                    
                    # 2. Get LLM response
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
