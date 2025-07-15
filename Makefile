.PHONY: install setup run clean test docker-build docker-run help

# Default target
help:
	@echo "🤖 CU Denver Blockchain Club AI - Available Commands:"
	@echo ""
	@echo "  make install    - Install Python dependencies"
	@echo "  make setup      - Setup documentation database"
	@echo "  make run        - Run the AI assistant"
	@echo "  make start      - Quick start (install + setup + run)"
	@echo "  make clean      - Clean generated files"
	@echo "  make docker     - Build and run with Docker"
	@echo "  make test       - Run basic health checks"
	@echo ""

# Install dependencies
install:
	@echo "📦 Installing Python dependencies..."
	pip3 install -r requirements.txt

# Setup documentation database
setup:
	@echo "📚 Setting up documentation database..."
	python3 setup_docs.py

# Run the application
run:
	@echo "🚀 Starting CU Denver Blockchain Club AI..."
	python3 app.py

# Quick start - everything in one command
start: install setup run

# Clean generated files
clean:
	@echo "🧹 Cleaning up..."
	rm -rf chroma_db/
	rm -rf __pycache__/
	rm -rf *.pyc
	rm -rf .pytest_cache/
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/

# Docker build and run
docker:
	@echo "🐳 Building Docker image..."
	docker build -t blockchain-club-ai .
	@echo "🚀 Running Docker container..."
	docker run -p 8000:8000 blockchain-club-ai

# Basic health checks
test:
	@echo "🔍 Running basic checks..."
	python3 -c "import fastapi, chromadb, requests; print('✅ All imports successful')"
	@echo "🐍 Python version:"
	python3 --version
	@echo "📦 Checking Ollama..."
	@which ollama > /dev/null && echo "✅ Ollama installed" || echo "❌ Ollama not found"
