from abc import ABC, abstractmethod
from typing import List, Dict
from shared.python.models.memory import MemoryRecord


class VectorStoreProvider(ABC):
    """
    Abstract interface for vector database operations.
    Allows seamlessly swapping Pinecone, Qdrant, Milvus, etc.
    """

    @abstractmethod
    async def store(self, memory: MemoryRecord) -> None:
        pass

    @abstractmethod
    async def get_by_owner(self, owner_id: str, limit: int) -> List[MemoryRecord]:
        pass

    @abstractmethod
    async def search(self, owner_id: str, query: str, limit: int) -> List[MemoryRecord]:
        pass

    @abstractmethod
    async def delete(self, memory_id: str) -> bool:
        pass


class InMemoryVectorStore(VectorStoreProvider):
    """
    Simple in-memory provider for rapid local development and testing
    before wiring up a production cloud database.
    """

    def __init__(self):
        self._storage: Dict[str, MemoryRecord] = {}

    async def store(self, memory: MemoryRecord) -> None:
        self._storage[memory.id] = memory

    async def get_by_owner(self, owner_id: str, limit: int) -> List[MemoryRecord]:
        results = [m for m in self._storage.values() if m.owner_id == owner_id]
        # Sort by creation time descending
        results.sort(key=lambda x: x.created_at, reverse=True)
        return results[:limit]

    async def search(self, owner_id: str, query: str, limit: int) -> List[MemoryRecord]:
        # A mock implementation of semantic search: just return all for owner for now
        # until we integrate LangChain/Embeddings
        return await self.get_by_owner(owner_id, limit)

    async def delete(self, memory_id: str) -> bool:
        if memory_id in self._storage:
            del self._storage[memory_id]
            return True
        return False
