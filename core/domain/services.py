from abc import ABC, abstractmethod

class GoogleDorkServicePort(ABC):
    @abstractmethod
    def search(self, query: str, num_results: int):
        pass
