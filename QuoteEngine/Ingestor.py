from typing import List
from .QuoteModel import QuoteModel
# from .DocxImporter import DocxImporter
# from .CSVImporter import CSVImporter
from .IngestorInterface import IngestorInterface


class Ingestor(IngestorInterface):
    importers = []

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)