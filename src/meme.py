import os
import random
import argparse

from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       # './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel.QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img_path=img, text=quote.body, author=quote.author, width=500)

    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    args = None
    parser = argparse.ArgumentParser(description='/pass img path,Quote ' + 'body, author')
    parser.add_argument('--path', type=str, default=None,
                        help='path of input image file')
    parser.add_argument('--body', type=str, default=None,
                        help='body of the quote')
    parser.add_argument('--author', type=str, default=None,
                        help='author of the quote')
    try:
        args = parser.parse_args()
    except:
        print("command line param not parsed")

    print(generate_meme(args.path, args.body, args.author))
