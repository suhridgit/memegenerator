from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TXTIngestor(IngestorInterface):

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        file_ref = open(path, "r", encoding="utf-8-sig")
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()

            if len(line) > 0:

                parse = line.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        file_ref.close()
        return quotes
