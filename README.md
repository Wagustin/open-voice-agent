# 🎙️ Open Voice Agent (Universal Voice Bridge & Spatial Companion)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg)](https://fastapi.tiangolo.com)
[![SwiftUI](https://img.shields.io/badge/iOS-SwiftUI-orange.svg)](https://developer.apple.com/xcode/swiftui/)
[![Jetpack Compose](https://img.shields.io/badge/Android-Jetpack--Compose-green.svg)](https://developer.android.com/jetpack/compose)

**Open Voice Agent** es una puerta de enlace de voz multimodal, ultra-rápida y privada que conecta tus dispositivos móviles (iOS / Android) con cualquier Agente de IA Autónomo (**Hermes Agent, Claude Code, Codex, OpenCode, Ollama, ChatGPT**).

---

## 🎯 Los 3 Modos de Uso (Perfiles de Usuario)

La aplicación está diseñada de forma modular para adaptarse a tres casos de uso clave:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 OPEN VOICE AGENT MODES                                 │
├───────────────────────────────────┬───────────────────────────────────┬────────────────┤
│ 1. 🎛️ Remote Control Mode          │ 2. 🎙️ Siri Replacement Mode       │ 3. 🌐 Combined │
│ (Dev & Agent Execution)           │ (Hands-Free Quick AI)             │ (Full Spatial) │
├───────────────────────────────────┼───────────────────────────────────┼────────────────┤
│ • Controla Claude Code, Codex u   │ • Asistente de voz de ultrabaja   │ • Control por  │
│   OpenCode desde tu móvil por voz.│   latencia (<1s) con Salomé TTS. │   voz + Siri   │
│ • Ejecuta tareas de programación, │ • Reemplaza a Siri activándolo    │   + Ubicación  │
│   scripts o comandos en tu PC.    │   con el Botón de Acción.         │   en 2º plano. │
└───────────────────────────────────┴───────────────────────────────────┴────────────────┘
```

1. **🎛️ Modo 1: Control a Distancia de Agente (Coding & Automation)**
   * Pensado para desarrolladores y usuarios avanzados.
   * Envía comandos por voz a tu laptop/servidor en casa para que tu agente de código (**Claude Code, Codex, OpenCode, Hermes**) programe, arregle bugs o ejecute scripts en segundo plano.

2. **🎙️ Modo 2: Reemplazo de Siri (Asistente de Voz Ultra-Rápido)**
   * Pensado para quienes buscan una experiencia de voz fluida y privada.
   * Respuesta en <1s mediante WebSockets con sintetizador de voz **Salomé (`es-CO-SalomeNeural`)** e interfaz flotante con Mesh FX (malla 3D reactiva).

3. **🌐 Modo 3: Asistente Completo Espacial (Control + Voz + Geolocalización)**
   * Combina la potencia del control de agente, las respuestas de voz tipo Siri y el módulo opcional de **geolocalización de bajo consumo (`CoreMotion` / `FusedLocation`)** para darle contexto de ubicación en tiempo real a tu IA.

---

## ✨ Características Principales

- 🎙️ **Full-Duplex Voice Tunnel:** Audio streaming bidireccional por WebSockets.
- 🔮 **UI 3D Reactiva (Mesh FX Shaders):** Orbe/Malla 3D interactiva que reacciona en tiempo real al micrófono y al audio del agente.
- 📍 **Módulo Opcional de Geolocalización:** Ingesta por lotes con consumo de batería cercano a cero gracias al coprocesador de movimiento del móvil.
- 🔘 **Push-to-Talk & Atajos:** Activación inmediata con el **Botón de Acción de iOS**, Widgets y Tiles de Ajustes Rápidos en Android.
- 🔌 **Universal Agent Adapters:** Conexión modular con Hermes, Claude Code, Codex, Ollama, Groq o ChatGPT.

---

## 🏗️ Arquitectura del Backend

```text
                               ┌────────────────────────────────────────────────────────┐
                               │             AGENT ADAPTERS (Enchufables)               │
                               ├────────────────────────────────────────────────────────┤
                               │ 1. HermesAdapter      ➔ Tu Servidor (Kathy)            │
[ App Móvil iOS/Android ]      │ 2. OpenAIAdapter      ➔ Ollama / Groq / ChatGPT / vLLM │
   │                │          │ 3. CLIProcessAdapter  ➔ Claude Code / Cursor / Codex   │
   │ (WebSocket)    │ (GPS Opt)│ 4. WebhookAdapter     ➔ Cualquier API o Bot custom     │
   ▼                ▼          └────────────────────────────────────────────────────────┘
 [ Open Voice Agent Server ] ─────────► [ STT Engine ] ──► [ Selected Agent ] ──► [ TTS Engine ]
 (FastAPI + WebSockets + DB)            (Whisper/Groq)                              (Edge-TTS/Salomé)
```

---

## 🚀 Inicio Rápido (Servidor Backend)

```bash
git clone https://github.com/Wagustin/open-voice-agent.git
cd open-voice-agent/backend

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

---

## 📱 Clientes Nativos (iOS & Android)

- 🍏 **iOS (`apps/ios/`):** Cliente Swift/SwiftUI con gestores para Action Button, AudioEngine y CoreMotion opcional.
- 🤖 **Android (`apps/android/`):** Servicio Kotlin con `AudioRecord`, `AudioTrack` y `FusedLocationProviderClient` opcional.

---

## 📜 Licencia

Desarrollado por **Agustín Ventura Saldaña**. Disponible bajo la Licencia MIT.
