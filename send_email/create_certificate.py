from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import os


def create_jpg(name):

    STATIC_DIR = str(os.path.join(Path(__file__).resolve().parent.parent, 'static'))
    attachment = os.path.join(STATIC_DIR, r'image\certificate-template.jpg')

    image = Image.open(attachment)
    font = ImageFont.truetype("arial.ttf", 90)
    drawer = ImageDraw.Draw(image)
    drawer.text((1150, 870), name, font=font, fill='black')

    image.save(STATIC_DIR + rf'\image\certificate-{name}.jpg')
