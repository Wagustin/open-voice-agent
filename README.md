# 🎙️📍 Open Voice Agent (Siri Replacement & Spatial AI Companion)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg)](https://fastapi.tiangolo.com)
[![SwiftUI](https://img.shields.io/badge/iOS-SwiftUI-orange.svg)](https://developer.apple.com/xcode/swiftui/)
[![Jetpack Compose](https://img.shields.io/badge/Android-Jetpack--Compose-green.svg)](https://developer.android.com/jetpack/compose)

**Open Voice Agent** es una puerta de enlace multimodal ultra-rápida y privada que convierte cualquier agente de IA autónomo (**Hermes Agent, Claude Code, Codex, OpenCode, Ollama**) en un asistente personal por voz con **conciencia espacial y geolocalización de bajo consumo en tiempo real**.

---

## ✨ Características Principales

- 🎙️ **Full-Duplex Voice Tunnel (Sub-segundo):** Comunicación por WebSockets con audio streaming de ultra-baja latencia (<1s) y respuesta hablada mediante la voz Salomé (`es-CO-SalomeNeural`).
- 📍 **Spatial Awareness & Battery-Optimized GPS Tracking:** Algoritmo integrado accionado por el coprocesador de movimiento del iPhone (`CoreMotion`) y Android (`FusedLocationProviderClient`) con consumo de batería cercano a cero.
- 🔮 **UI 3D Reactiva (Mesh FX Shaders):** Visualizador flotante con ondas y malla 3D (estilo Siri / Cyberpunk) que reacciona a la amplitud de voz de tu micrófono y de la respuesta de la IA.
- 🔘 **Push-to-Talk & Hardware Integration:** Activación inmediata con el **Botón de Acción de iOS**, Widgets y Tiles de Ajustes Rápidos en Android.
- 🔌 **Universal Agent Adapter System:** Conexión modular transparente con Hermes Agent (Kathy), Claude Code, Codex, Ollama y APIs en la nube.

---

## 🏗️ Arquitectura del Sistema

```text
                               ┌────────────────────────────────────────────────────────┐
                               │             AGENT ADAPTERS (Enchufables)               │
                               ├────────────────────────────────────────────────────────┤
                               │ 1. HermesAdapter      ➔ Tu Servidor (Kathy)            │
[ App Móvil iOS/Android ]      │ 2. OpenAIAdapter      ➔ Ollama / Groq / ChatGPT / vLLM │
   │                │          │ 3. CLIProcessAdapter  ➔ Claude Code / Cursor / Codex   │
   │ (WebSocket)    │ (GPS)    │ 4. WebhookAdapter     ➔ Cualquier API o Bot custom     │
   ▼                ▼          └────────────────────────────────────────────────────────┘
 [ Open Voice Agent Server ] ─────────► [ STT Engine ] ──► [ Selected Agent ] ──► [ TTS Engine ]
 (FastAPI + WebSockets + DB)            (Whisper/Groq)                              (Edge-TTS/Salomé)
```

---

## 🚀 Inicio Rápido (Servidor Backend)

### 1. Requisitos
- Python 3.10+
- Linux / macOS / Windows Server

### 2. Instalación
```bash
git clone https://github.com/Wagustin/open-voice-agent.git
cd open-voice-agent/backend

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Ejecutar el Servidor
```bash
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

---

## 📱 Clientes Móviles (Nativos)

- 🍏 **iOS (`apps/ios/`):** Proyecto SwiftUI listo para Xcode con soporte para Action Button, CoreLocation y CoreMotion.
- 🤖 **Android (`apps/android/`):** Servicio Kotlin con `AudioRecord`, `AudioTrack` y `FusedLocationProviderClient`.

---

## 📜 Licencia

Desarrollado por **Agustín Ventura Saldaña**. Bajo la Licencia MIT.
