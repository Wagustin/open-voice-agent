import Foundation

struct AgentSettings {
    private static let serverKey = "open_voice_agent_server_url"
    private static let apiKeyKey = "open_voice_agent_api_key"
    
    // Default fallback (can be overwritten in App Settings or via 1-Prompt pairing)
    static let defaultServerURL = "http://100.120.75.115:8001"
    static let defaultApiKey = "kathy-voice-secure-token"
    
    static var serverBaseURL: String {
        get {
            UserDefaults.standard.string(forKey: serverKey) ?? defaultServerURL
        }
        set {
            UserDefaults.standard.set(newValue, forKey: serverKey)
        }
    }
    
    static var apiKey: String {
        get {
            UserDefaults.standard.string(forKey: apiKeyKey) ?? defaultApiKey
        }
        set {
            UserDefaults.standard.set(newValue, forKey: apiKeyKey)
        }
    }
    
    static var locationHttpURL: URL {
        let base = serverBaseURL.trimmingCharacters(in: CharacterSet(charactersIn: "/"))
        return URL(string: "\(base)/api/v1/location/update") ?? URL(string: "\(defaultServerURL)/api/v1/location/update")!
    }
    
    static var voiceWebSocketURL: URL {
        let base = serverBaseURL.trimmingCharacters(in: CharacterSet(charactersIn: "/"))
        let wsScheme = base.hasPrefix("https://") ? base.replacingOccurrences(of: "https://", with: "wss://") : base.replacingOccurrences(of: "http://", with: "ws://")
        return URL(string: "\(wsScheme)/ws/voice") ?? URL(string: "ws://100.120.75.115:8001/ws/voice")!
    }
}
