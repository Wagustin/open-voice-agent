import Foundation
import CoreLocation
import CoreMotion

class LocationManager: NSObject, ObservableObject, CLLocationManagerDelegate {
    private let locationManager = CLLocationManager()
    private let motionActivityManager = CMMotionActivityManager()
    
    @Published var lastLocation: CLLocation?
    @Published var currentActivity: String = "stationary"
    @Published var isTracking: Bool = false
    
    private var serverURL: URL { AgentSettings.locationHttpURL }
    private var apiKey: String { AgentSettings.apiKey }
    
    override init() {
        super.init()
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyBestForNavigation
        locationManager.distanceFilter = 10.0 // Meter threshold for low battery drain
        locationManager.allowsBackgroundLocationUpdates = true
        locationManager.pausesLocationUpdatesAutomatically = true
    }
    
    func startTracking() {
        locationManager.requestAlwaysAuthorization()
        locationManager.startUpdatingLocation()
        locationManager.startMonitoringSignificantLocationChanges()
        startMotionTracking()
        isTracking = true
    }
    
    func stopTracking() {
        locationManager.stopUpdatingLocation()
        motionActivityManager.stopActivityUpdates()
        isTracking = false
    }
    
    private func startMotionTracking() {
        if CMMotionActivityManager.isActivityAvailable() {
            motionActivityManager.startActivityUpdates(to: .main) { [weak self] activity in
                guard let activity = activity else { return }
                if activity.walking { self?.currentActivity = "walking" }
                else if activity.running { self?.currentActivity = "running" }
                else if activity.automotive { self?.currentActivity = "automotive" }
                else if activity.cycling { self?.currentActivity = "cycling" }
                else if activity.stationary { self?.currentActivity = "stationary" }
            }
        }
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        guard let location = locations.last else { return }
        self.lastLocation = location
        sendLocationToServer(location: location)
    }
    
    private func sendLocationToServer(location: CLLocation) {
        var request = URLRequest(url: serverURL)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.setValue(apiKey, forHTTPHeaderField: "X-API-Key")
        
        let payload: [String: Any] = [
            "device_id": UIDevice.current.identifierForVendor?.uuidString ?? "ios-device",
            "latitude": location.coordinate.latitude,
            "longitude": location.coordinate.longitude,
            "altitude": location.altitude,
            "accuracy": location.horizontalAccuracy,
            "speed": location.speed,
            "heading": location.course,
            "activity_type": currentActivity,
            "battery_level": UIDevice.current.batteryLevel
        ]
        
        request.httpBody = try? JSONSerialization.data(withJSONObject: payload)
        URLSession.shared.dataTask(with: request).resume()
    }
}
