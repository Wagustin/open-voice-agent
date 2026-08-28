import Foundation
import AVFoundation
import Combine

class VoiceAgentManager: NSObject, ObservableObject, URLSessionWebSocketDelegate {
    private var webSocketTask: URLSessionWebSocketTask?
    private let audioEngine = AVAudioEngine()
    private var audioPlayer: AVAudioPlayer?
    
    @Published var isListening: Bool = false
    @Published var isSpeaking: Bool = false
    @Published var transcriptText: String = ""
    @Published var agentResponseText: String = ""
    
    private let wsURL = URL(string: "ws://100.120.75.115:8001/ws/voice")!
    
    func connect() {
        let session = URLSession(configuration: .default, delegate: self, delegateQueue: OperationQueue())
        webSocketTask = session.webSocketTask(with: wsURL)
        webSocketTask?.resume()
        receiveMessages()
    }
    
    func triggerActionButton() {
        // Called when hardware Action Button or App Shortcut is pressed
        if isListening {
            stopListeningAndSend()
        } else {
            startListening()
        }
    }
    
    func startListening() {
        let audioSession = AVAudioSession.sharedInstance()
        try? audioSession.setCategory(.playAndRecord, mode: .default, options: [.defaultToSpeaker, .allowBluetooth])
        try? audioSession.setActive(true)
        
        isListening = true
        transcriptText = "Escuchando..."
        
        let inputNode = audioEngine.inputNode
        let recordingFormat = inputNode.outputFormat(forBus: 0)
        
        inputNode.installTap(onBus: 0, bufferSize: 1024, format: recordingFormat) { [weak self] buffer, time in
            // Send audio PCM buffer over WebSocket
        }
        
        audioEngine.prepare()
        try? audioEngine.start()
    }
    
    func stopListeningAndSend() {
        audioEngine.stop()
        audioEngine.inputNode.removeTap(onBus: 0)
        isListening = false
        
        let payload: [String: Any] = [
            "type": "user_transcript",
            "text": transcriptText
        ]
        
        if let data = try? JSONSerialization.data(withJSONObject: payload),
           let jsonString = String(data: data, encoding: .utf8) {
            webSocketTask?.send(.string(jsonString)) { _ in }
        }
    }
    
    private func receiveMessages() {
        webSocketTask?.receive { [weak self] result in
            switch result {
            case .success(let message):
                switch message {
                case .string(let text):
                    self?.handleTextMessage(text)
                case .data(let audioData):
                    self?.playAudioResponse(data: audioData)
                @unknown default:
                    break
                }
                self?.receiveMessages()
            case .failure(let error):
                print("WebSocket error: \(error)")
            }
        }
    }
    
    private func handleTextMessage(_ text: String) {
        guard let data = text.data(using: .utf8),
              let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any] else { return }
        
        DispatchQueue.main.async {
            if let type = json["type"] as? String, type == "agent_response_text" {
                self.agentResponseText = json["text"] as? String ?? ""
            }
        }
    }
    
    private func playAudioResponse(data: Data) {
        DispatchQueue.main.async {
            self.isSpeaking = true
            self.audioPlayer = try? AVAudioPlayer(data: data)
            self.audioPlayer?.play()
        }
    }
}
