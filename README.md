# 🎙️ Open Voice Agent (1-Prompt Agent Pairing & Spatial Voice Companion)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg)](https://fastapi.tiangolo.com)
[![SwiftUI](https://img.shields.io/badge/iOS-SwiftUI-orange.svg)](https://developer.apple.com/xcode/swiftui/)
[![Jetpack Compose](https://img.shields.io/badge/Android-Jetpack--Compose-green.svg)](https://developer.android.com/jetpack/compose)

**Open Voice Agent** es una puerta de enlace de voz multimodal, ultra-rápida y privada que conecta tus dispositivos móviles (iOS / Android) con cualquier Agente de IA Autónomo (**Hermes Agent, Claude Code, Codex, OpenCode, Ollama, ChatGPT**) mediante un **único prompt de vinculación automática**.

---

## 🪄 Vinculación en 1 Solo Prompt (Zero Manual Setup)

El usuario no necesita configurar manualmente servidores, archivos `.env` ni claves complejas:

```text
[ 1. Abre la App Móvil ] ──► [ 2. Copia el Master Prompt ] ──► [ 3. Pega el Prompt a su Agente ] ──► [ 4. ¡Vinculado! ]
Genera un Token de         "Configura Open Voice Agent        El Agente (Claude/Hermes/Codex)      Voz en 1-tap y
vinculación único.         para conectarte con mi app..."     ejecuta la instalación solo.         UI 3D lista.
```

### 📄 El Master Prompt:
> *"Hola Agente, quiero conectarme contigo por voz desde mi iPhone/Android. Ejecuta este comando para instalar el backend y vincularte con mi token de seguridad `[MI_TOKEN]`:*
>
> `curl -fsSL https://raw.githubusercontent.com/Wagustin/open-voice-agent/main/install.sh | bash -s -- --token [MI_TOKEN]`
>
> *Confírmame cuando el WebSocket esté activo en el puerto 8001 para empezar a hablar."*

---

## 🎯 Los 3 Modos de Uso

1. **🎛️ Modo 1: Control a Distancia de Agente (Coding & Automation)**
   * Envía comandos por voz a tu laptop/servidor para que tu agente de código (**Claude Code, Codex, OpenCode, Hermes**) programe, arregle bugs o ejecute scripts en segundo plano.

2. **🎙️ Modo 2: Reemplazo de Siri (Asistente de Voz Ultra-Rápido)**
   * Respuesta en <1s mediante WebSockets con sintetizador de voz **Salomé (`es-CO-SalomeNeural`)** e interfaz flotante con Mesh FX (malla 3D reactiva).

3. **🌐 Modo 3: Asistente Completo Espacial (Control + Voz + Geolocalización)**
   * Combina la potencia del control de agente, las respuestas de voz tipo Siri y el módulo opcional de **geolocalización de bajo consumo (`CoreMotion` / `FusedLocation`)** para darle contexto espacial en tiempo real a tu IA.

---

## 🏗️ Arquitectura del Backend

```text
                               ┌────────────────────────────────────────────────────────┐
                               │             AGENT ADAPTERS (Enchufables)               │
                               ├────────────────────────────────────────────────────────┤
                               │ 1. HermesAdapter      ➔ Tu Servidor (Kathy)            │
[ App Móvil iOS/Android ]      │ 2. OpenAIAdapter      ➔ Ollama / Groq / ChatGPT / vLLM │
   │                │          │ 3. CLIProcessAdapter  ➔ Claude Code / Cursor / Codex   │
   │ (WebSocket)    │ (GPS Opt)│ 4. WebhookAdapter     ➔ Cualquier API or Bot custom    │
   ▼                ▼          └────────────────────────────────────────────────────────┘
 [ Open Voice Agent Server ] ─────────► [ STT Engine ] ──► [ Selected Agent ] ──► [ TTS Engine ]
 (FastAPI + WebSockets + DB)            (Whisper/Groq)                              (Edge-TTS/Salomé)
```

---

## 📱 Clientes Nativos (iOS & Android)

- 🍏 **iOS (`apps/ios/`):** Cliente Swift/SwiftUI con `AppShortcutsProvider` para vinculación automática con el **Botón de Acción del iPhone** sin tutoriales manuales.
- 🤖 **Android (`apps/android/`):** Servicio Kotlin con `AudioRecord`, `AudioTrack` y Tile de Ajustes Rápidos.

---

## 📜 Licencia

Desarrollado por **Agustín Ventura Saldaña**. Disponible bajo la Licencia MIT.
