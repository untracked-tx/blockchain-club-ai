#!/bin/bash

# 🚀 CU Denver Blockchain Club AI - MacBook Startup Script
echo "🤖 Starting CU Denver Blockchain Club AI Assistant..."

# Check if Ollama is running
if ! pgrep -x "ollama" > /dev/null; then
    echo "🔄 Starting Ollama..."
    ollama serve &
    sleep 3
fi

# Check if model exists
if ! ollama list | grep -q "llama3-chatqa"; then
    echo "📥 Downloading llama3-chatqa model..."
    ollama pull llama3-chatqa
fi

# Setup docs if needed
if [ ! -d "./chroma_db" ]; then
    echo "📚 Setting up documentation database..."
    python3 setup_docs.py
fi

# Start the AI assistant
echo "🚀 Starting AI Assistant on localhost:8000..."
echo "💡 Use 'ngrok http 8000' in another terminal to make it public"
python3 app.py
