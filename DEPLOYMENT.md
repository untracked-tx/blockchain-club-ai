# 🚀 Deployment Guide - CU Denver Blockchain Club AI

## 🍎 MacBook Quick Start (Recommended)

### One-Command Setup
```bash
git clone https://github.com/untracked-tx/blockchain-club-ai.git && cd blockchain-club-ai && chmod +x start_macbook.sh && ./start_macbook.sh
```

### What the script does:
1. ✅ Checks if Python 3 and pip are installed
2. ✅ Installs Ollama (if not already installed)
3. ✅ Downloads the llama3-chatqa model
4. ✅ Installs Python dependencies
5. ✅ Sets up the documentation database
6. ✅ Starts the AI assistant on localhost:8000

### Making it Public (Optional)
In another terminal:
```bash
# Install ngrok if you haven't already
brew install ngrok

# Make your local server public
ngrok http 8000
```

## 🔧 Manual Setup (If Script Fails)

### Prerequisites
1. **Python 3.8+** - Check with `python3 --version`
2. **Homebrew** - Install from https://brew.sh
3. **Git** - Should be pre-installed on macOS

### Step-by-Step Installation

#### 1. Install Ollama
```bash
brew install ollama
```

#### 2. Start Ollama and Download Model
```bash
# Start Ollama in background
ollama serve &

# Download the model (this will take a few minutes)
ollama pull llama3-chatqa
```

#### 3. Clone and Setup Project
```bash
git clone https://github.com/untracked-tx/blockchain-club-ai.git
cd blockchain-club-ai
pip3 install -r requirements.txt
```

#### 4. Setup Documentation Database
```bash
python3 setup_docs.py
```

#### 5. Run the Application
```bash
python3 app.py
```

### 🌐 Access Points
- **API**: http://localhost:8000
- **Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### Setup Steps

#### 1. Install Ollama & Model
```bash
# Download Ollama from https://ollama.ai
# Then pull the model:
ollama pull llama3-chatqa
```

#### 2. Clone & Setup Project
```bash
git clone https://github.com/untracked-tx/blockchain-club-ai.git
cd blockchain-club-ai
pip install -r requirements.txt
```

#### 3. Setup Database
```bash
python setup_docs.py
```

#### 4. Run the Application
```bash
python app.py
```

#### 5. Make it Public (Optional)
```bash
# In another terminal:
ngrok http 8000
```

Copy the ngrok URL and update your main site to point to it.

### Environment Variables (Optional)
```bash
export OLLAMA_HOST=http://localhost:11434
export PORT=8000
```

### Troubleshooting
- **Ollama not found**: Make sure Ollama is running (`ollama serve`)
- **Model not found**: Run `ollama pull llama3-chatqa`
- **Port in use**: Change port in app.py or kill process using port 8000
- **No documents**: Make sure `user-guide/` folder exists with .md files

### API Endpoints
- `GET /` - Health check
- `POST /ask` - Ask questions
- `GET /health` - System status
