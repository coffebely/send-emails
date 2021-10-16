from pathlib import Path
import requests
import os
from .text import text, title


def send_simple_message(email, name):
    MEDIA_DIR = str(os.path.join(Path(__file__).resolve().parent.parent, 'static'))
    attachment = os.path.join(MEDIA_DIR, f'image\certificate-{name}.jpg')
    return requests.post(
        "https://api.mailgun.net/v3/YOUR_DOMAIN/messages",
        auth=("api", "YOUR_API_KEY"),
        data={"from": "YOUR_DOMAIN",
              "to": [f"{email}"],
              "subject": title,
              "text": text},
        files=[("attachment", open(attachment, 'rb'))])
