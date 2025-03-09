import chromadb
from chromadb.utils import embedding_functions
from typing import Dict, Any, List
from core.config import settings

class ChromaService:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=settings.CHROMA_PATH)
        self.embedder = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )

    def get_user_collection(self, api_key: str):
        return self.client.get_or_create_collection(
            name=f"user_{api_key}",
            embedding_function=self.embedder,
            metadata={"hnsw:space": "cosine"}
        )

    def get_collection(self, collection_name: str):
        return self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedder,
            metadata={"hnsw:space": "cosine"}
        )

    async def add_document(self, document_id: str, data: Dict[str, Any], collection: str = "default"):
        collection = self.get_collection(collection)
        document_text = self._format_data(data)
        embeddings =  self.embedder([document_text])  # Generate embeddings
        collection.add(
            ids=document_id,
            documents=document_text,
            metadatas=data,  # Store original data as metadata
            embeddings=embeddings  # Store embeddings in FAISS
        )

    async def search(self, query: str, collection: str = "default", n_results: int = 10) -> List[Dict[str, Any]]:
        collection = self.get_collection(collection)
        results = collection.query(
            query_texts=[query],
            n_results=n_results,
            include=["metadatas", "distances"]
        )
        return [
            {
                "id": results["ids"][0][i],
                "data": results["metadatas"][0][i],
                "score": 1 - results["distances"][0][i]
            }
            for i in range(len(results["ids"][0]))
        ]

    def _format_data(self, data: Dict[str, Any]) -> str:
        """Convert JSON data to searchable text"""
        return " ".join(
            f"{key} {value}" for key, value in self._flatten_dict(data).items()
        )

    def _flatten_dict(self, d: Dict, parent_key: str = '') -> Dict:
        """Flatten nested dictionaries"""
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}_{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(self._flatten_dict(v, new_key).items())
            else:
                items.append((new_key, str(v)))
        return dict(items)