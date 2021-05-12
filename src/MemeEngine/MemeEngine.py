from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine(object):

    def __init__(self, out_path):
        self.out_path = out_path

    def make_meme(self, img_path, text, author, width=500) -> str:

        img = Image.open(img_path)

        if width is not None:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        message = text + ' - ' + author
        if message is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            draw.text((10, 30), message, font=font, fill='white')

        from pathlib import Path

        current = Path('.').resolve()

        outputfile = f'./{random.randint(0,100000000)}.jpg'
        filepath = current / self.out_path / outputfile

        try:
            img.save(filepath)
        except ValueError:
            print(ValueError)

        return filepath
