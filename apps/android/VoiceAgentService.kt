package com.openagent.voice

import android.app.Service
import android.content.Intent
import android.media.*
import android.os.IBinder
import okhttp3.*
import okio.ByteString
import org.json.JSONObject
import java.util.concurrent.Executors

class VoiceAgentService : Service() {

    private lateinit var webSocket: WebSocket
    private val client = OkHttpClient()
    private val executor = Executors.newSingleThreadExecutor()
    private var isRecording = false

    override func onCreate() {
        super.onCreate()
        initWebSocket()
    }

    private fun initWebSocket() {
        val request = Request.Builder()
            .url("ws://100.120.75.115:8001/ws/voice")
            .build()

        webSocket = client.newWebSocket(request, object : WebSocketListener() {
            override fun onMessage(webSocket: WebSocket, text: String) {
                // Process text message from server
            }

            override fun onMessage(webSocket: WebSocket, bytes: ByteString) {
                // Play audio bytes received from Edge-TTS (Salomé voice)
                playAudioResponse(bytes.toByteArray())
            }
        })
    }

    fun startVoiceSession() {
        isRecording = true
        executor.execute {
            val sampleRate = 16000
            val bufferSize = AudioRecord.getMinBufferSize(
                sampleRate,
                AudioFormat.CHANNEL_IN_MONO,
                AudioFormat.ENCODING_PCM_16BIT
            )

            val audioRecord = AudioRecord(
                MediaRecorder.AudioSource.MIC,
                sampleRate,
                AudioFormat.CHANNEL_IN_MONO,
                AudioFormat.ENCODING_PCM_16BIT,
                bufferSize
            )

            val buffer = ByteArray(bufferSize)
            audioRecord.startRecording()

            while (isRecording) {
                val read = audioRecord.read(buffer, 0, buffer.size)
                if (read > 0) {
                    webSocket.send(ByteString.of(buffer, 0, read))
                }
            }

            audioRecord.stop()
            audioRecord.release()
        }
    }

    private fun playAudioResponse(audioData: ByteArray) {
        val audioTrack = AudioTrack.Builder()
            .setAudioAttributes(
                AudioAttributes.Builder()
                    .setUsage(AudioAttributes.USAGE_MEDIA)
                    .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
                    .build()
            )
            .setAudioFormat(
                AudioFormat.Builder()
                    .setEncoding(AudioFormat.ENCODING_PCM_16BIT)
                    .setSampleRate(16000)
                    .setChannelMask(AudioFormat.CHANNEL_OUT_MONO)
                    .build()
            )
            .setBufferSizeInBytes(audioData.size)
            .build()

        audioTrack.write(audioData, 0, audioData.size)
        audioTrack.play()
    }

    override fun onBind(intent: Intent?): IBinder? = null
}
