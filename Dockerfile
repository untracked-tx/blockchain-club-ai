FROM python:3.9

RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# Install Ollama
USER root
RUN curl -fsSL https://ollama.ai/install.sh | sh
USER user

COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY --chown=user . /app


# Create startup script
USER root
RUN echo '#!/bin/bash\nollama serve &\nsleep 15\nollama pull llama3-chatqa\npython setup_docs.py\nexec uvicorn app:app --host 0.0.0.0 --port 7860' > /app/start.sh
RUN chmod +x /app/start.sh
USER user

CMD ["/app/start.sh"]
