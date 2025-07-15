from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import chromadb
from sentence_transformers import SentenceTransformer
import os
from typing import List

app = FastAPI(
    title="CU Denver Blockchain Club AI", 
    description="AI-powered documentation chatbot for the CU Denver Blockchain Club's on-chain membership system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
chroma_client = chromadb.PersistentClient(path="./chroma_db")
embedder = SentenceTransformer('all-MiniLM-L6-v2')

class QueryRequest(BaseModel):
    question: str
    context: str = ""  # Optional context from your site

class QueryResponse(BaseModel):
    answer: str
    sources: List[str]
    confidence: float

def query_ollama(prompt: str) -> str:
    """Query local Ollama instance"""
    try:
        response = requests.post("http://localhost:11434/api/generate", 
                               json={
                                   "model": "llama3-chatqa",
                                   "prompt": prompt,
                                   "stream": False
                               },
                               timeout=60)
        
        if response.status_code == 200:
            return response.json()['response']
        else:
            return f"Error: Ollama returned status {response.status_code}. Make sure Ollama is running with 'ollama serve'"
    except requests.exceptions.ConnectionError:
        return "Error: Cannot connect to Ollama. Please make sure Ollama is running with 'ollama serve'"
    except requests.exceptions.Timeout:
        return "Error: Ollama request timed out. The model might be too large or busy."
    except Exception as e:
        return f"Error: {str(e)}"

def search_docs(query: str, top_k: int = 3):
    """Search for relevant documents"""
    try:
        collection = chroma_client.get_collection(name="tech_docs")
        query_embedding = embedder.encode([query]).tolist()
        
        results = collection.query(
            query_embeddings=query_embedding,
            n_results=top_k
        )
        
        relevant_docs = []
        for i in range(len(results['documents'][0])):
            relevant_docs.append({
                'text': results['documents'][0][i],
                'source': results['metadatas'][0][i]['source'],
                'distance': results['distances'][0][i]
            })
        
        return relevant_docs
    except Exception as e:
        print(f"Search error: {e}")
        return []

@app.get("/")
def root():
    return {
        "status": "CU Denver Blockchain Club AI is running", 
        "endpoints": ["/ask", "/health", "/docs-status"],
        "docs": "/docs"
    }

@app.post("/ask", response_model=QueryResponse)
async def ask_question(request: QueryRequest):
    """Main endpoint for asking questions"""
    try:
        # Search for relevant documents
        relevant_docs = search_docs(request.question)
        
        # Create context
        context = "\n\n".join([doc['text'] for doc in relevant_docs])
        
        # Add any additional context from the site
        if request.context:
            context = f"Page context: {request.context}\n\nDocumentation:\n{context}"
        
        # Create prompt
        system_prompt = """You are the official AI assistant for UC Denver Blockchain Club. You help new members join and understand our blockchain platform.

PERSONALITY:
- Friendly and welcoming (like a helpful club member)
- Patient with beginners who know nothing about crypto
- Enthusiastic about the club's mission
- Never condescending about blockchain knowledge

GUIDELINES:
- Always prioritize user safety and security
- If unsure about financial advice, direct to human support
- Use simple language, avoid technical jargon
- Celebrate when users complete steps
- Address common concerns: cost, safety, complexity

CONTEXT: You have access to club documentation. Use it to give specific, accurate answers about our platform, smart contracts, and membership process."""

        prompt = f"""{system_prompt}

Documentation Context:
{context}

User Question: {request.question}

Helpful Answer:"""
        
        # Get answer from Ollama
        answer = query_ollama(prompt)
        
        # Calculate confidence based on relevance scores
        avg_distance = sum([doc['distance'] for doc in relevant_docs]) / len(relevant_docs) if relevant_docs else 1.0
        confidence = max(0.0, min(1.0, 1.0 - avg_distance))
        
        # Get unique sources
        sources = list(set([doc['source'] for doc in relevant_docs]))
        
        return QueryResponse(
            answer=answer,
            sources=sources,
            confidence=confidence
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    try:
        collection = chroma_client.get_collection(name="tech_docs")
        doc_count = collection.count()
        return {
            "status": "healthy", 
            "documents": doc_count,
            "model": "llama3-chatqa",
            "ollama_connection": "✅ Connected"
        }
    except Exception as e:
        return {"status": "initializing", "error": str(e)}

@app.get("/docs-status")
async def docs_status():
    """Check documentation loading status"""
    try:
        collection = chroma_client.get_collection(name="tech_docs")
        return {"loaded": True, "count": collection.count()}
    except:
        return {"loaded": False, "count": 0}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
