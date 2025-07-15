import os
import chromadb

def setup_documentation():
    """Setup ChromaDB with user-guide documentation only"""
    print("🔧 Setting up documentation database for user-guide files...")
    
    # Initialize ChromaDB
    client = chromadb.PersistentClient(path="./chroma_db")
    
    # Create or recreate collection
    try:
        client.delete_collection("tech_docs")
        print("♻️  Cleared existing collection")
    except:
        pass
    
    collection = client.create_collection("tech_docs")
    
    # Only process user-guide directory
    user_guide_path = "./user-guide"
    
    if not os.path.exists(user_guide_path):
        print(f"❌ Error: {user_guide_path} directory not found!")
        return
    
    documents = []
    metadatas = []
    ids = []
    
    print(f"📂 Processing files in {user_guide_path}...")
    
    for root, dirs, files in os.walk(user_guide_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # Skip empty files
                        if content.strip():
                            documents.append(content)
                            metadatas.append({
                                "source": file_path.replace("\\", "/"),
                                "filename": file,
                                "directory": "user-guide"
                            })
                            ids.append(f"doc_{len(documents)}")
                            print(f"✅ Added: {file}")
                        else:
                            print(f"⚠️  Skipped empty file: {file}")
                            
                except Exception as e:
                    print(f"❌ Error reading {file_path}: {e}")
    
    if documents:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"🎉 Successfully added {len(documents)} documents to database")
        print("📝 Documents are ready for AI queries!")
    else:
        print("❌ No documents found in user-guide directory")

if __name__ == "__main__":
    setup_documentation()
