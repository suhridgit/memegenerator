from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import pandas as pd
from typing import List


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_cat = QuoteModel(row['body'], row['author'])
            quotes.append(new_cat)

        return quotes
