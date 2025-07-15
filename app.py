from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import chromadb
import requests
import json
import uvicorn

app = FastAPI(title="CU Denver Blockchain Club AI Assistant")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://untrackedtx.xyz",
        "https://*.ngrok-free.app",  # Allow all ngrok domains
        "https://*.ngrok.io",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

class Question(BaseModel):
    question: str

def search_documents(query: str, n_results: int = 3):
    """Search for relevant documents using ChromaDB"""
    try:
        collection = client.get_collection("docs")
        results = collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results['documents'][0] if results['documents'] else []
    except Exception as e:
        print(f"Search error: {e}")
        return []

def query_llama(prompt: str) -> str:
    """Query llama3-chatqa model via Ollama"""
    try:
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': 'llama3-chatqa',
                'prompt': prompt,
                'stream': False,
                'options': {
                    'temperature': 0.7,
                    'top_p': 0.9,
                    'max_tokens': 500
                }
            }
        )
        
        if response.status_code == 200:
            return response.json()['response']
        else:
            return "Sorry, I'm having trouble connecting to the AI model."
            
    except Exception as e:
        print(f"Llama query error: {e}")
        return "Sorry, I encountered an error while processing your question."

@app.post("/ask")
async def ask_question(request: Question):
    try:
        # Search for relevant documents from user-guide only
        relevant_docs = search_documents(request.question)
        context = "\n\n".join(relevant_docs) if relevant_docs else "No specific documentation found."
        
        # Create optimized prompt
        system_prompt = """You are the official AI assistant for CU Denver Blockchain Club. Your role is to help members join and navigate our blockchain membership platform.

CORE IDENTITY:
- Friendly club representative who makes blockchain accessible
- Patient educator for crypto beginners
- Enthusiastic about decentralized technology
- Safety-first approach to all recommendations

RESPONSE STYLE:
- Use simple, clear language (avoid: "utilize", "facilitate", "leverage")
- Break complex topics into digestible steps
- Include specific next actions when possible
- Acknowledge user concerns directly

SAFETY PROTOCOLS:
- Never provide specific financial advice or price predictions
- Always emphasize "do your own research" for investments
- Direct complex technical issues to: Liam.Murphy@ucdenver.edu
- Warn about common scams (fake airdrops, impersonation, etc.)

CLUB CONTEXT:
- We focus on education, not speculation
- Membership is on-chain via smart contracts
- Community values: transparency, security, learning

When answering:
1. Address the user's specific question first
2. Provide relevant club/technical details from documentation
3. Suggest logical next steps
4. Offer to clarify or expand on any point

Documentation Context: {context}

User Question: {question}

Response:"""

        prompt = system_prompt.format(context=context, question=request.question)
        
        # Get answer from Llama 3.1 8B
        answer = query_llama(prompt)
        
        return {
            "question": request.question,
            "answer": answer,
            "sources_found": len(relevant_docs)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model": "llama3-chatqa", "docs_source": "user-guide"}

@app.get("/")
async def root():
    return {"message": "CU Denver Blockchain Club AI Assistant", "docs": "/docs"}

if __name__ == "__main__":
    print("🚀 Starting CU Denver Blockchain Club AI Assistant...")
    print("📱 Use ngrok to make it public: ngrok http 8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
