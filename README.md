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
- 🤖 **Android (`apps/android/`):** Servicio Kotlin con `VoiceInteractionService` (Asistente digital nativo del sistema) y Tile de Ajustes Rápidos.

---

## 🛡️ Estrategia de Publicación & Cumplimiento (App Store & Google Play)

Para permitir que **Open Voice Agent** viva tanto como un sistema **100% privado y self-hosted** como una **aplicación pública aprobable en las tiendas oficiales**, la arquitectura se diseñó bajo los siguientes principios:

### 1. 🔄 Arquitectura de Conexión Desacoplada (`AgentSettings`)
* La app móvil no tiene IPs fijas congeladas en el código binario.
* **Modo Privado:** El usuario vincula su servidor personal (vía Tailscale, Cloudflare Tunnel o IP local) con 1 solo prompt o escaneo QR.
* **Modo Tienda (App Review):** Para la revisión de Apple y Google, la app incluye una pantalla de bienvenida con un **Servidor Demo Público HTTPS/WSS** y modo offline de demostración, garantizando que el revisor humano pueda probar el audio y la interfaz sin configurar un servidor propio (evitando el rechazo automático por Guideline 2.1).

### 2. 🤖 Android (Google Play Store)
* **Reemplazo Nativo del Asistente:** A diferencia de iOS, Android permite oficialmente reemplazar al asistente digital del sistema mediante `VoiceInteractionService` y el rol `ROLE_ASSISTANT`. El usuario puede configurar Open Voice Agent como asistente predeterminado desde los Ajustes del teléfono.
* **Ubicación y Micrófono sin Bloqueos:** En lugar de solicitar `ACCESS_BACKGROUND_LOCATION` (que exige justificaciones manuales en video), el tracking y el audio se ejecutan bajo un **Foreground Service** con notificación persistente (`foregroundServiceType="location|microphone"`). Al ser visible para el usuario, Google Play lo aprueba de forma estándar.

### 3. 🍏 iOS (Apple App Store)
* **Integración Oficial con el Sistema:** Apple prohíbe explícitamente apps que afirmen "suplantar o reemplazar a Siri". La integración se realiza legalmente mediante **App Intents** y atajos configurados en el **Botón de Acción (Action Button)** del iPhone 15 Pro / 16.
* **App Transport Security (ATS):** Todo el tráfico móvil en producción utiliza estrictamente **HTTPS** y **WSS** (WebSockets Secure).
* **Privacy Manifest (`PrivacyInfo.xcprivacy`):** Inclusión obligatoria del manifiesto declarando las razones de acceso a APIs requeridas (`UserDefaults`, `CoreMotion`, geolocalización de bajo consumo con `startMonitoringSignificantLocationChanges`).

---

## 📜 Licencia

Desarrollado por **Agustín Ventura Saldaña**. Disponible bajo la Licencia MIT.

