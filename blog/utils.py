import os
import random
import re
import string
import unicodedata

from flask import current_app
from PIL import Image

from blog import app

UPLOAD_FOLDER = app.config["UPLOAD_FOLDER"]

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 6


def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))


def slugify(value):
    value = str(value)
    value = (
        unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    )
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "-", value)


def title_slugifier(post_title):
    slug = slugify(post_title) + "-" + generate_random_string()
    return slug


def save_picture(form_data):
    filename = form_data.filename
    picture_name = generate_random_string() + "-" + filename
    picture_path = os.path.join(current_app.root_path, UPLOAD_FOLDER, picture_name)

    image = Image.open(form_data)
    image.save(picture_path)

    return picture_name
