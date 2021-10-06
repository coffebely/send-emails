from pathlib import Path
import requests
import os
from .text import text, title


def send_simple_message(email,  name):
    MEDIA_DIR = str(os.path.join(Path(__file__).resolve().parent.parent, 'media'))
    attachment = os.path.join(MEDIA_DIR, f'certificate-{name}.jpg')
    return requests.post(
        "https://api.mailgun.net/v3/sandbox9533174d59624751a515752235e0f2c3.mailgun.org/messages",
        auth=("api", "b4067df9b14b6b473a0865341d43fc82-443ec20e-0a52789b"),
        data={"from": "mailgun@sandbox9533174d59624751a515752235e0f2c3.mailgun.org",
              "to": [f"{email}"],
              "subject": title,
              "text": text},
        files=[("attachment", open(attachment, 'rb'))])
