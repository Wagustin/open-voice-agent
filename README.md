# 🎙️ OpenVoice Assistant (`open-voice-agent`)

**Sub-second latency, privacy-first Siri replacement & hands-free voice interface for local AI Agents.**

[Español](#-visión-en-español) | [English](#-english-overview)

---

## 🇪🇸 Visión en Español

`OpenVoice Assistant` es un cliente móvil y servidor de transmisión de voz en tiempo real de código abierto diseñado para reemplazar asistentes comerciales (como Siri o Google Assistant) por un agente de Inteligencia Artificial propio, autónomo y privado.

### 🚀 Características Principales
* **Latencia Sub-Segundo (< 1 segundo):** Comunicación en tiempo real vía WebSockets con transmisión continua de audio (Full-Duplex Streaming).
* **Integración con Botón de Acción & Widgets (iOS/Android):** Activación instantánea con un toque desde la pantalla de bloqueo o el botón lateral.
* **Pipeline de Procesamiento de Voz:**
  1. **STT (Speech-to-Text):** Transcripción ultrarrápida con Whisper / Groq API.
  2. **Cerebro (LLM Engine):** Procesamiento contextual con Hermes Agent / Ollama / OpenAI.
  3. **TTS (Text-to-Speech):** Síntesis de voz natural y fluida en alta definición (edge-tts / Salomé voice).
* **Soporte Manos Libres:** Detección de palabra de activación (*"Oye Kathy"*) y visualización de ondas de audio interactivas.

### 🏗️ Arquitectura de Audio
```text
📱 App Móvil (Voice UI / Action Button)
       │
       └── (Audio Stream vía WebSockets) ──► 🐍 Engine (FastAPI + Asyncio)
                                                     │
                                                     ├──► 🎙️ Whisper STT
                                                     ├──► 🧠 Hermes Agent / LLM
                                                     └──► 🔊 Edge-TTS (Audio Out)
```

---

## 🇬🇧 English Overview

`OpenVoice Assistant` is a real-time, low-latency voice client and server framework built as an open-source Siri replacement for local and autonomous AI agents.

### 🌟 Key Features
* **Sub-Second Latency:** Full-duplex WebSocket audio streaming for natural conversation flow.
* **Hands-Free & Action Button Ready:** Native iOS Widget and Action Button bindings for instant activation.
* **Modular Pipeline:** Plug-and-play support for Whisper STT, LLM engines, and high-fidelity TTS systems.

---

## 🛠️ Quick Start

### 1. Server Engine Setup
```bash
git clone https://github.com/Wagustin/open-voice-agent.git
cd open-voice-agent/server
pip install -r requirements.txt
python main.py
```

---

## 📜 License
MIT License © 2026 [Agustín Ventura Saldaña](https://github.com/Wagustin) & Kathy AI Core.
