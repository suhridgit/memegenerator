"""
Quote model class returns the representation of the
quotes as body - author
"""


class QuoteModel():

    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr(self):
        """ Returns the quote in the body-author format"""
        return f'{self.body} - {self.author}'
