# 🛠️ Troubleshooting Guide

## Common Issues and Solutions

### 1. "Permission denied" when running start_macbook.sh

**Solution:**
```bash
chmod +x start_macbook.sh
./start_macbook.sh
```

### 2. "Ollama not found" or "command not found: ollama"

**Solution:**
```bash
# Install Ollama via Homebrew
brew install ollama

# Or download directly from ollama.ai
curl -fsSL https://ollama.ai/install.sh | sh
```

### 3. "Cannot connect to Ollama" error

**Solution:**
```bash
# Start Ollama service
ollama serve &

# Wait a few seconds, then test
ollama list
```

### 4. Python dependency issues

**Solution:**
```bash
# Update pip first
pip3 install --upgrade pip

# Install dependencies with verbose output
pip3 install -r requirements.txt -v

# If still failing, try creating a virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. "Model not found" error

**Solution:**
```bash
# Pull the model manually
ollama pull llama3-chatqa

# Check if it's available
ollama list
```

### 6. Port 8000 already in use

**Solution:**
```bash
# Find what's using port 8000
lsof -i :8000

# Kill the process (replace PID)
kill -9 <PID>

# Or use a different port
python3 app.py --port 8001
```

### 7. ChromaDB database issues

**Solution:**
```bash
# Remove and recreate the database
rm -rf chroma_db/
python3 setup_docs.py
```

### 8. Slow model responses

**Reason:** The llama3-chatqa model might be slow on older MacBooks.

**Solutions:**
- Use a smaller model: `ollama pull llama3.2:1b`
- Update the model in `app.py` and `start_macbook.sh`
- Or upgrade to a newer MacBook with more RAM

### 9. Memory issues

**Symptoms:** System becomes slow or unresponsive

**Solutions:**
- Close other applications
- Use a smaller model (1B instead of 3B)
- Increase swap space
- Add more RAM if possible

### 10. ngrok issues

**Solution:**
```bash
# Install ngrok
brew install ngrok

# Sign up for free account at ngrok.com
ngrok authtoken YOUR_TOKEN

# Start tunnel
ngrok http 8000
```

## 🔍 Health Check Commands

```bash
# Check if Python is working
python3 --version

# Check if all dependencies are installed
python3 -c "import fastapi, chromadb, requests, sentence_transformers; print('✅ All good')"

# Check if Ollama is running
ollama list

# Check if documentation database exists
ls -la chroma_db/

# Test the API
curl http://localhost:8000/health
```

## 📞 Getting Help

If you're still having issues:

1. **Check the logs** - Look for error messages in the terminal output
2. **Restart everything** - Sometimes a fresh start helps
3. **Update your system** - Make sure macOS and Homebrew are up to date
4. **Contact support** - Email Liam.Murphy@ucdenver.edu with your error logs

## 💡 Performance Tips

- **Use SSD storage** for better ChromaDB performance
- **Close other AI apps** to free up memory
- **Use wired internet** for faster model downloads
- **Keep your MacBook plugged in** for sustained performance
