import re
from .models import Person
from pathlib import Path
import os
import csv
from .create_certificate import create_jpg
from .send_email import send_simple_message
import time
from email.utils import formatdate


def handler(file):
    MEDIA_DIR = str(os.path.join(Path(__file__).resolve().parent.parent, 'media'))

    with open(os.path.join(MEDIA_DIR, file)) as f:
        reader = csv.reader(f)
        for row in reader:
            instance = Person(name=row[0] + ' ' + row[1], email=row[2])
            instance.save()
            create_jpg(instance.name)
            send_simple_message(instance.email, instance.name)

    time.sleep(60)
    return True


def limit(file):
    MEDIA_DIR = str(os.path.join(Path(__file__).resolve().parent.parent, 'media'))

    with open(os.path.join(MEDIA_DIR, file)) as f:
        reader = csv.reader(f)
        return len(list(reader))


def time_now():
    return formatdate()


def chek_file(file):
    MEDIA_DIR = str(os.path.join(Path(__file__).resolve().parent.parent, 'media'))

    with open(os.path.join(MEDIA_DIR, file)) as f:
        reader = csv.reader(f)
        email = []
        for row in reader:

            email.append(row[2])
            regexp = re.compile(r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$', re.IGNORECASE)
            email_chek = regexp.findall(row[2])
            name = row[0] + row[1]

            if not name.isalpha():
                return False
            if not email_chek:
                return False

        if len(email) != len(set(email)):
            return False
        return True
