#!/bin/bash

# 🚀 CU Denver Blockchain Club AI - MacBook Startup Script
echo "🤖 Starting CU Denver Blockchain Club AI Assistant..."
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if Python 3 is installed
if ! command_exists python3; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    echo "💡 You can install it via Homebrew: brew install python"
    exit 1
fi

# Check if Homebrew is installed
if ! command_exists brew; then
    echo "❌ Homebrew not found. Installing Homebrew first..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Check if Ollama is installed
if ! command_exists ollama; then
    echo "❌ Ollama is not installed. Installing via Homebrew..."
    brew install ollama
    echo "✅ Ollama installed"
fi

# Create and activate virtual environment
echo "🐍 Setting up Python virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install Python dependencies
echo "� Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Start Ollama service (this runs in background)
echo ""
echo "🦙 Setting up Ollama..."
if ! pgrep -x "ollama" > /dev/null; then
    echo "🔄 Starting Ollama service..."
    ollama serve &
    echo "⏳ Waiting for Ollama to start (10 seconds)..."
    sleep 10
else
    echo "✅ Ollama is already running"
fi

# Check if model exists and pull if needed
echo "🔍 Checking for llama3-chatqa model..."
if ! ollama list | grep -q "llama3-chatqa"; then
    echo "📥 Downloading llama3-chatqa model..."
    echo "⚠️  This will take 5-10 minutes depending on your internet speed"
    ollama pull llama3-chatqa
    echo "✅ Model downloaded successfully"
else
    echo "✅ llama3-chatqa model already available"
fi

# Setup documentation database
if [ ! -d "./chroma_db" ]; then
    echo "📚 Setting up documentation database..."
    python setup_docs.py
    echo "✅ Documentation database ready"
else
    echo "✅ Documentation database already exists"
fi

# Start the AI assistant
echo ""
echo "🎉 Everything is ready!"
echo "🚀 Starting AI Assistant on localhost:8000..."
echo "� API docs will be available at: http://localhost:8000/docs"
echo "🔍 Health check at: http://localhost:8000/health"
echo ""
echo "💡 To make it public, run this in another terminal:"
echo "   brew install ngrok && ngrok http 8000"
echo ""
echo "🛑 Press Ctrl+C to stop the server"
echo ""

python app.py
