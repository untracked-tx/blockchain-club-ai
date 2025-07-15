# 🤖 CU Denver Blockchain Club AI Assistant

An AI-powered documentation chatbot for the CU Denver Blockchain Club's on-chain membership system. Built with FastAPI, ChromaDB, and Ollama, it provides intelligent, context-aware answers about smart contracts, technical documentation, and blockchain protocols.

**🌐 Live Demo**: [untrackedtx.xyz](https://untrackedtx.xyz)

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
- **Ollama** - Local AI model serving (llama3-chatqa)
- **Python 3.8+** - Core application language
- **Docker** - Containerization for easy deployment

## 🚀 Setup Instructions

### Prerequisites

- **macOS** with Python 3.8+
- **Homebrew** package manager
- **Ollama** for local AI model serving
- **ngrok** (optional, for public access)

### Installation Steps

1. **Install Ollama and download the model**
   ```bash
   brew install ollama
   ollama serve &
   ollama pull llama3-chatqa
   ```

2. **Clone the repository**
   ```bash
   git clone https://github.com/untracked-tx/blockchain-club-ai.git
   cd blockchain-club-ai
   ```

3. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Python dependencies**
   ```bash
   pip install --upgrade pip wheel setuptools
   pip install -r requirements.txt
   ```

5. **Set up the documentation database**
   ```bash
   python setup_docs.py
   ```

6. **Start the application**
   ```bash
   python app.py
   ```

7. **Make it publicly accessible (optional)**
   ```bash
   # In another terminal
   ngrok http 8000
   ```

Your AI assistant will be running at `http://localhost:8000`

### Alternative: Docker Deployment

```bash
# Build and run with Docker
docker build -t blockchain-club-ai .
docker run -p 8000:8000 blockchain-club-ai
```

## 📖 API Usage

### Ask a Question

```bash
curl -X POST "http://localhost:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "How does the membership smart contract work?"}'
```

**Response:**
```json
{
  "question": "How does the membership smart contract work?",
  "answer": "The membership smart contract implements...",
  "sources_found": 3
}
```

### Health Check

```bash
curl http://localhost:8000/health
```

### Interactive API Documentation

Visit `http://localhost:8000/docs` for the interactive Swagger UI.

## 📁 Project Structure

```
blockchain-club-ai/
├── app.py                    # Main FastAPI application
├── setup_docs.py            # ChromaDB setup script
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker configuration
├── DEPLOYMENT.md           # Additional deployment info
├── user-guide/            # Documentation source files
│   ├── 1-PROJECT-OVERVIEW.md
│   ├── 2-FRONTEND-GUIDE.md
│   ├── 3-ONBOARDING-NAVIGATION.md
│   ├── 4-SMART-CONTRACTS.md
│   ├── AI-CHATBOT-GUIDE.md
│   └── doc-breakdown.md
└── chroma_db/             # Vector database (auto-generated)
```

## 🔧 Configuration

Optional environment variables:

- `PORT` - Server port (default: 8000)
- `HOST` - Server host (default: 0.0.0.0)
- `OLLAMA_HOST` - Ollama server URL (default: http://localhost:11434)

## 📚 About the Project

This chatbot serves the **CU Denver Blockchain Club**, supporting education and development in:

- **Crypto Investing Education** - Investment strategies and market analysis
- **Blockchain Technology** - Decentralized systems and protocols
- **On-Chain Membership** - Smart contract-based membership systems
- **Smart Contract Development** - Ethereum contract building and auditing

### 🔗 Links

- **Live Demo**: [untrackedtx.xyz](https://untrackedtx.xyz)
- **Main Repository**: [blockchain-club](https://github.com/untracked-tx/blockchain-club)
- **Contact**: Liam.Murphy@ucdenver.edu

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🤝 Contributing

Contributions welcome! Fork the repo, create a feature branch, and submit a pull request.

---

*Built for the CU Denver Blockchain Club*
