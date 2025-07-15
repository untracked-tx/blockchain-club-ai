# 🚀 Deployment Guide

## MacBook Plug-and-Play Setup

### Super Quick Start (One Command)
```bash
git clone https://github.com/untracked-tx/blockchain-club-ai.git && cd blockchain-club-ai && ./start_macbook.sh
```

Then in another terminal:
```bash
ngrok http 8000
```

### Manual Setup Steps

#### 1. Install Ollama
```bash
brew install ollama
ollama serve &
ollama pull llama3.1:8b
```

#### 2. Clone & Setup Project
```bash
git clone https://github.com/untracked-tx/blockchain-club-ai.git
cd blockchain-club-ai
pip3 install -r requirements.txt
python3 setup_docs.py
```

#### 3. Run the Application
```bash
python3 app.py
```

#### 4. Make it Public
```bash
# In another terminal:
ngrok http 8000
```

Copy the ngrok URL and update your main site to point to it.

## Running on Other Devices

### Prerequisites
1. **Python 3.8+** installed
2. **Ollama** installed with Llama 3.1 8B model
3. **ngrok** (for public access)

### Setup Steps

#### 1. Install Ollama & Model
```bash
# Download Ollama from https://ollama.ai
# Then pull the model:
ollama pull llama3.1:8b
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
- **Model not found**: Run `ollama pull llama3.1:8b`
- **Port in use**: Change port in app.py or kill process using port 8000
- **No documents**: Make sure `user-guide/` folder exists with .md files

### API Endpoints
- `GET /` - Health check
- `POST /ask` - Ask questions
- `GET /health` - System status
