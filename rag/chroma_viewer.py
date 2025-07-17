import chromadb

client = chromadb.PersistentClient(path="db/chroma_db")  # Use the directory, not the sqlite file
print(client.list_collections())


collection = client.get_collection("langchain")  # Default collection name for LangChain

# View all documents and metadata
results = collection.get(include=["documents", "metadatas"])
print(results["documents"])      # List of document texts
print(results["metadatas"])      # Associated metadata
print(results["ids"])            # Document IDs