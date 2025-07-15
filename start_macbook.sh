#!/bin/bash

# 🚀 CU Denver Blockchain Club AI - MacBook Startup Script
echo "🤖 Starting CU Denver Blockchain Club AI Assistant..."

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

# Check if pip is installed
if ! command_exists pip3; then
    echo "❌ pip3 is not installed. Please install pip first."
    exit 1
fi

# Check if Ollama is installed
if ! command_exists ollama; then
    echo "❌ Ollama is not installed. Installing via Homebrew..."
    if command_exists brew; then
        brew install ollama
    else
        echo "❌ Homebrew not found. Please install Ollama manually:"
        echo "💡 Visit: https://ollama.ai/download"
        exit 1
    fi
fi

# Check if Ollama is running
if ! pgrep -x "ollama" > /dev/null; then
    echo "🔄 Starting Ollama..."
    ollama serve &
    sleep 5
    echo "⏳ Waiting for Ollama to start..."
fi

# Check if model exists and pull if needed
echo "🔍 Checking for Llama model..."
if ! ollama list | grep -q "llama3-chatqa"; then
    echo "📥 Downloading llama3-chatqa model (this may take a few minutes)..."
    ollama pull llama3-chatqa
else
    echo "✅ llama3-chatqa model already available"
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

# Setup docs if needed
if [ ! -d "./chroma_db" ]; then
    echo "📚 Setting up documentation database..."
    python3 setup_docs.py
else
    echo "✅ Documentation database already exists"
fi

# Start the AI assistant
echo ""
echo "🚀 Starting AI Assistant on localhost:8000..."
echo "💡 In another terminal, run 'ngrok http 8000' to make it public"
echo "🌐 API docs will be available at: http://localhost:8000/docs"
echo ""
python3 app.py
