# 🤖 Blockchain Club Documentation Chatbot

An AI-powered documentation chatbot for the **CU Denver** Blockchain Club's on-chain membership system. This FastAPI-based application provides intelligent, context-aware responses about the club's technical documentation, smart contracts, and blockchain protocols.

**🌐 Live Demo**: Available at [untrackedtx.xyz](https://untrackedtx.xyz) via ngrok tunnel

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

## 🚀 Quick Start (MacBook Optimized)

### Prerequisites

- **macOS** with Python 3.8+
- **Ollama** installed
- **ngrok** account (for public access)

### One-Command Setup

```bash
# 1. Install Ollama (if not installed)
brew install ollama

# 2. Start Ollama and pull model
ollama serve &
ollama pull llama3-chatqa

# 3. Clone and setup project
git clone https://github.com/untracked-tx/blockchain-club-ai.git
cd blockchain-club-ai
pip3 install -r requirements.txt
python3 setup_docs.py

# 4. Start the AI assistant
python3 app.py &

# 5. Make it public with ngrok
ngrok http 8000
```

**🎉 That's it!** Copy the ngrok URL and update untrackedtx.xyz to point to it.

### Manual Step-by-Step

1. **Install Ollama**
   ```bash
   brew install ollama
   ollama serve
   ```

2. **In another terminal, pull the model**
   ```bash
   ollama pull llama3-chatqa
   ```

3. **Clone the repository**
   ```bash
   git clone https://github.com/untracked-tx/blockchain-club-ai.git
   cd blockchain-club-ai
   ```

4. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Set up the documentation database**
   ```bash
   python3 setup_docs.py
   ```

6. **Run the application**
   ```bash
   python3 app.py
   ```

7. **In another terminal, start ngrok**
   ```bash
   ngrok http 8000
   ```

The API will be available locally at `http://localhost:8000` and publicly via the ngrok URL.

### Using Docker

```bash
# Build the image
docker build -t blockchain-club-ai .

# Run the container
docker run -p 8000:8000 blockchain-club-ai
```

### Public Access with ngrok

```bash
# In another terminal (after starting the app):
ngrok http 8000
```

Then update your website to point to the ngrok URL.

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
├── app.py                    # Main FastAPI application
├── setup_docs.py            # Setup script (user-guide only)
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker configuration
├── DEPLOYMENT.md           # Deployment guide for other devices
├── user-guide/            # Blockchain club documentation
│   ├── 1-PROJECT-OVERVIEW.md
│   ├── 2-FRONTEND-GUIDE.md
│   ├── 3-ONBOARDING-NAVIGATION.md
│   ├── 4-SMART-CONTRACTS.md
│   ├── AI-CHATBOT-GUIDE.md
│   └── doc-breakdown.md   # Complete GitHub docs reference
└── chroma_db/             # Vector database (auto-generated)
```

## 🔧 Configuration

The application can be configured through environment variables:

- `PORT` - Server port (default: 8000)
- `HOST` - Server host (default: 0.0.0.0)

## 📚 About the CU Denver Blockchain Club

This chatbot serves the **CU Denver Blockchain Club**, which focuses on:

- **Crypto Investing Education** - Teaching investment strategies and market analysis
- **Blockchain Technology** - Exploring decentralized systems and protocols
- **On-Chain Membership** - Implementing blockchain-based membership systems
- **Smart Contract Development** - Building and auditing Ethereum contracts

### 🔗 Related Projects

- **Main Club Project**: [blockchain-club](https://github.com/untracked-tx/blockchain-club) - The core membership system and smart contracts
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

- CU Denver Blockchain Club members
- The broader blockchain and cryptocurrency community
- Contributors to the open-source AI and vector database ecosystem

---

*Built with ❤️ for the blockchain community*
