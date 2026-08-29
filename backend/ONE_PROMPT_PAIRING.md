# 🪄 The 1-Prompt Agent Pairing & Setup Flow

Con **Open Voice Agent**, el usuario no necesita configurar manualmente servidores, IPs ni archivos `.env`. Su propio Agente de IA (Claude Code, Codex, Hermes, OpenCode) realiza la instalación y vinculación automáticamente mediante **un solo prompt**.

---

## 📱 Flujo del Usuario (Step-by-Step)

```text
[ 1. Abre la App Móvil ] ──► [ 2. Copia el Master Prompt ] ──► [ 3. Pega el Prompt a su Agente ] ──► [ 4. ¡Vinculado! ]
Genera un Token de         "Configura Open Voice Agent        El Agente ejecuta el setup          Voz en 1-tap y
vinculación único.         para conectarte con mi app..."     y confirma la conexión.            UI 3D lista.
```

---

## 📄 El Master Prompt (Lo que el usuario le da a su Agente):

> *"Hola Agente, quiero conectarme contigo por voz desde mi iPhone/Android usando Open Voice Agent. Ejecuta este comando para instalar el servidor backend y vincularte con mi token de seguridad `[TOKEN_UNICO]`:*
>
> ```bash
> curl -fsSL https://raw.githubusercontent.com/Wagustin/open-voice-agent/main/install.sh | bash -s -- --token [TOKEN_UNICO]
> ```
>
> *Una vez instalado, confírmame que el servidor WebSocket está corriendo en el puerto 8001 para empezar a hablar por voz."*

---

## ⚙️ ¿Qué hace el Agente en segundo plano cuando recibe este prompt?

1. Descarga e inicia el contenedor/servidor ultraligero de **`open-voice-agent`**.
2. Registra el token de autenticación del dispositivo móvil.
3. Notifica por WebSocket a la App Móvil: **"Agente vinculado con éxito"**.
4. ¡El iPhone/Android vibra, suena el "pip" 🔔 y el Orbe 3D se activa de inmediato!
