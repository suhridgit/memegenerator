from typing import List
import subprocess
import os

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path)-> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        quotes = []
        cmd = ["./xpdf-tools-mac-4.03/bin64/pdftotext", path]

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        output, _ = process.communicate()
        output = output.splitlines()

        for item in output:
            quote, author = item.split('-')
            a_quote = QuoteModel(quote, author)
            quotes.append(a_quote)

        return quotes
