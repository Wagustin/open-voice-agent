package com.openagent.voice

import android.content.Context

object AgentSettings {
    private const val PREFS_NAME = "open_voice_agent_prefs"
    private const val KEY_SERVER_URL = "server_base_url"
    private const val KEY_API_KEY = "api_key"
    
    // Default fallback (can be customized via settings UI or 1-prompt pairing QR)
    const val DEFAULT_SERVER = "http://100.120.75.115:8001"
    const val DEFAULT_API_KEY = "kathy-voice-secure-token"

    fun getServerBaseUrl(context: Context): String {
        val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
        return prefs.getString(KEY_SERVER_URL, DEFAULT_SERVER) ?: DEFAULT_SERVER
    }

    fun setServerBaseUrl(context: Context, url: String) {
        val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
        prefs.edit().putString(KEY_SERVER_URL, url.trimEnd('/')).apply()
    }

    fun getApiKey(context: Context): String {
        val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
        return prefs.getString(KEY_API_KEY, DEFAULT_API_KEY) ?: DEFAULT_API_KEY
    }

    fun setApiKey(context: Context, key: String) {
        val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
        prefs.edit().putString(KEY_API_KEY, key.trim()).apply()
    }

    fun getHttpLocationUrl(context: Context): String {
        val base = getServerBaseUrl(context).trimEnd('/')
        return "$base/api/v1/location/update"
    }

    fun getVoiceWebSocketUrl(context: Context): String {
        val base = getServerBaseUrl(context).trimEnd('/')
        val wsScheme = if (base.startsWith("https://")) {
            base.replace("https://", "wss://")
        } else {
            base.replace("http://", "ws://")
        }
        return "$wsScheme/ws/voice"
    }
}
