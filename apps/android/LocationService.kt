package com.openagent.voice

import android.app.Service
import android.content.Intent
import android.location.Location
import android.os.IBinder
import android.os.Looper
import com.google.android.gms.location.*
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONObject
import java.util.concurrent.Executors

class LocationService : Service() {

    private lateinit var fusedLocationClient: FusedLocationProviderClient
    private lateinit var locationCallback: LocationCallback
    private val httpClient = OkHttpClient()
    private val executor = Executors.newSingleThreadExecutor()

    override func onCreate() {
        super.onCreate()
        fusedLocationClient = LocationServices.getFusedLocationProviderClient(this)

        val locationRequest = LocationRequest.Builder(Priority.PRIORITY_BALANCED_POWER_ACCURACY, 15000)
            .setMinUpdateDistanceMeters(10f)
            .build()

        locationCallback = object : LocationCallback() {
            override fun onLocationResult(locationResult: LocationResult) {
                for (location in locationResult.locations) {
                    sendLocationToServer(location)
                }
            }
        }

        fusedLocationClient.requestLocationUpdates(locationRequest, locationCallback, Looper.getMainLooper())
    }

    private fun sendLocationToServer(location: Location) {
        executor.execute {
            try {
                val json = JSONObject().apply {
                    put("device_id", android.os.Build.MODEL)
                    put("latitude", location.latitude)
                    put("longitude", location.longitude)
                    put("altitude", location.altitude)
                    put("accuracy", location.accuracy)
                    put("speed", location.speed)
                    put("activity_type", "automotive")
                }

                val body = json.toString().toRequestBody("application/json".toMediaType())
                val request = Request.Builder()
                    .url("http://100.120.75.115:8001/api/v1/location/update")
                    .addHeader("X-API-Key", "kathy-voice-secure-token")
                    .post(body)
                    .build()

                httpClient.newCall(request).execute().close()
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }

    override fun onBind(intent: Intent?): IBinder? = null

    override fun onDestroy() {
        super.onDestroy()
        fusedLocationClient.removeLocationUpdates(locationCallback)
    }
}
