#!/usr/bin/env bash
set -e

echo "🚀 Installing Open Voice Agent Server..."

TOKEN=""
PORT=8001

while [[ $# -gt 0 ]]; do
  case $1 in
    --token)
      TOKEN="$2"
      shift 2
      ;;
    --port)
      PORT="$2"
      shift 2
      ;;
    *)
      shift
      ;;
  esac
done

if [ -z "$TOKEN" ]; then
  TOKEN="ova-agent-token-$(date +%s)"
fi

INSTALL_DIR="$HOME/.open-voice-agent"
mkdir -p "$INSTALL_DIR"

echo "📂 Target directory: $INSTALL_DIR"

if [ -d "$INSTALL_DIR/.git" ]; then
  echo "🔄 Updating existing Open Voice Agent installation..."
  git -C "$INSTALL_DIR" pull --quiet
else
  echo "📥 Cloning repository..."
  git clone --quiet https://github.com/Wagustin/open-voice-agent.git "$INSTALL_DIR"
fi

cd "$INSTALL_DIR/backend"

if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is required."
    exit 1
fi

if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate
pip install -r requirements.txt --quiet

export VOICE_API_KEY="$TOKEN"

echo "✨ Open Voice Agent Server successfully configured!"
echo "🔑 Token: $TOKEN"
echo "🌐 Starting server on port $PORT..."

exec uvicorn main:app --host 0.0.0.0 --port "$PORT"
