# 🤖 CU Denver Blockchain Club AI Assistant

> An AI-powered documentation chatbot for the CU Denver Blockchain Club's on-chain membership system. Built with FastAPI, ChromaDB, and Ollama, it provides intelligent, context-aware answers about smart contracts, technical docs, and blockchain protocols. Includes easy MacBook deployment, RESTful API, and semantic search.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**🌐 Live Demo**: Available at [untrackedtx.xyz](https://untrackedtx.xyz)

## 🚀 Features

- **Intelligent Document Search**: Vector-based semantic search through comprehensive blockchain club documentation
- **AI-Powered Responses**: Context-aware answers using advanced language models
- **Technical Documentation**: Covers smart contracts, security audits, gas analysis, and system architecture
- **RESTful API**: Clean, documented API endpoints for integration
- **Vector Database**: ChromaDB for efficient document retrieval and semantic search

## 📋 What's Included

The chatbot has access to comprehensive documentation about:

- **Smart Contract Architecture** - Technical specifications and implementation details
- **Security Framework** - Audit results and security best practices
- **Gas Analysis** - Performance optimization and cost analysis
- **Whitepaper** - Complete technical specification of the membership protocol
- **Code Quality Reports** - Static analysis and compliance documentation

## 🛠️ Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **ChromaDB** - Vector database for semantic search
- **Python** - Core application language
- **Docker** - Containerization for easy deployment

## 🚀 Quick Start (MacBook) 

### One-Command Setup 🎯
```bash
git clone https://github.com/untracked-tx/blockchain-club-ai.git && cd blockchain-club-ai && chmod +x start_macbook.sh && ./start_macbook.sh
```

**What the script does:**
1. ✅ Checks for Python 3 and Homebrew (installs if missing)
2. ✅ Installs Ollama (if needed)
3. ✅ Creates Python virtual environment
4. ✅ Installs Python dependencies in venv
5. ✅ Starts Ollama service in background
6. ✅ Downloads llama3-chatqa model (5-10 min first time)
7. ✅ Sets up documentation database
8. ✅ Starts API server on localhost:8000

### Make it Public (Optional)
```bash
# In another terminal
brew install ngrok
ngrok http 8000
```

### Manual Setup (if script fails)

1. **Prerequisites**
   ```bash
   # Install Homebrew (if not already installed)
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Install Ollama
   brew install ollama
   ```

2. **Clone and Setup**
   ```bash
   git clone https://github.com/untracked-tx/blockchain-club-ai.git
   cd blockchain-club-ai
   
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Start Ollama and Download Model**
   ```bash
   # Start Ollama (runs in background)
   ollama serve &
   
   # Download model (takes 5-10 minutes first time)
   ollama pull llama3-chatqa
   ```

4. **Setup Database and Run**
   ```bash
   # Setup documentation database
   python setup_docs.py
   
   # Start the API
   python app.py
   ```

### Using Docker
```bash
docker build -t blockchain-club-ai .
docker run -p 8000:8000 blockchain-club-ai
```

### Using Make Commands
```bash
make help        # See all available commands
make start       # Quick start (install + setup + run)
make clean       # Clean up generated files
```

## 📖 API Usage

### Ask a Question

```bash
curl -X POST "http://localhost:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "How does the membership smart contract work?"}'
```

### Health Check

```bash
curl http://localhost:8000/health
```

## 📁 Project Structure

```
blockchain-club-ai/
├── 📱 app.py                    # Main FastAPI application
├── 🛠️ setup_docs.py             # Documentation database setup  
├── 🍎 start_macbook.sh          # MacBook one-click startup script
├── 📦 requirements.txt          # Python dependencies
├── 🐳 Dockerfile               # Docker configuration
├── 🔧 Makefile                 # Development commands
├── 📚 user-guide/              # Blockchain club documentation
│   ├── 1-PROJECT-OVERVIEW.md
│   ├── 2-FRONTEND-GUIDE.md  
│   ├── 3-ONBOARDING-NAVIGATION.md
│   └── 4-SMART-CONTRACTS.md
├── 🗄️ chroma_db/               # Vector database (auto-generated)
├── 🔍 .gitignore               # Git ignore rules
└── 🛠️ TROUBLESHOOTING.md       # Common issues and solutions
```

## 🔧 Configuration

### Understanding Ollama
- **Ollama** is a local AI server that runs the language model
- **`ollama serve`** starts the server (runs in background)
- **`ollama pull llama3-chatqa`** downloads the AI model (one-time, ~4GB)
- **The model runs locally** - no internet needed after download

### Environment Variables
- `PORT` - Server port (default: 8000)
- `HOST` - Server host (default: 0.0.0.0)

## 🛠️ Troubleshooting

**Common Issues:**
- **Permission denied**: Run `chmod +x start_macbook.sh`
- **Ollama not found**: Install with `brew install ollama`
- **Port 8000 in use**: Check with `lsof -i :8000` and kill the process
- **Model not downloading**: Ensure stable internet connection

For detailed troubleshooting, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

## 🎯 API Endpoints

| Endpoint | Method | Description |
|----------|---------|-------------|
| `/` | GET | API status and info |
| `/ask` | POST | Ask questions about blockchain docs |
| `/health` | GET | Health check and system status |
| `/docs-status` | GET | Documentation database status |
| `/docs` | GET | Interactive API documentation |

## 📚 About the Blockchain Club

This chatbot serves the **University of Colorado Denver Blockchain Club**, which focuses on:

- **Crypto Investing Education** - Teaching investment strategies and market analysis
- **Blockchain Technology** - Exploring decentralized systems and protocols
- **On-Chain Membership** - Implementing blockchain-based membership systems
- **Smart Contract Development** - Building and auditing Ethereum contracts

For more information about the club:
- **Website**: https://untrackedtx.xyz (includes live chatbot demo)
- **Contact**: Liam.Murphy@ucdenver.edu

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- University of Colorado Denver Blockchain Club members
- The broader blockchain and cryptocurrency community
- Contributors to the open-source AI and vector database ecosystem

---

*Built with ❤️ for the blockchain community*
