from abc import ABC, abstractmethod

class BaseParser(ABC):
    name: str

    @abstractmethod
    def fetch(self) -> str:
        pass

    @abstractmethod
    def parse(self, raw: str) -> list[dict]:
        pass

    @abstractmethod
    def save(self, items: list[dict]) -> None:
        pass

    def run(self):
        raw = self.fetch()
        items = self.parse(raw)
        if items:
            self.save(items)
