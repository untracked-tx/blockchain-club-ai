FROM python:3.11

# Create non-root user
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# Install system dependencies as root
USER root
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    cmake \
    rustc \
    cargo \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.ai/install.sh | sh

# Switch back to user
USER user

# Copy requirements and install Python dependencies
COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip wheel setuptools
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy application code
COPY --chown=user . /app

# Create startup script
USER root
RUN echo '#!/bin/bash\n\
echo "🚀 Starting CU Denver Blockchain Club AI in Docker..."\n\
echo "⏳ Starting Ollama service..."\n\
ollama serve &\n\
sleep 15\n\
echo "📥 Downloading llama3-chatqa model..."\n\
ollama pull llama3-chatqa\n\
echo "📚 Setting up documentation database..."\n\
python setup_docs.py\n\
echo "🌐 Starting API server on port 8000..."\n\
exec uvicorn app:app --host 0.0.0.0 --port 8000' > /app/start.sh

RUN chmod +x /app/start.sh
USER user

EXPOSE 8000

CMD ["/app/start.sh"]
