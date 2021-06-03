#!/usr/bin/env python3

from glob import iglob
from os.path import abspath, expanduser, expandvars, join
from pprint import pprint as pp
from typing import Any

from PIL import Image
from PIL.ExifTags import TAGS as EXIF_TAGS

from .config import settings


def initialise():
    pass


def get_image_list():
    out = []
    for image_store in settings.image_stores:
        image_store = abspath(expanduser(expandvars(image_store)))
        print(image_store)
        for f in iglob(join(image_store, '**/*.JPG'), recursive=True):
            out.append(f)
    return out


def process(image_file_name: str):
    with Image.open(image_file_name) as image:
        return get_exif_data(image)


def key_of(d: dict, value: Any):
    for k, v in d.items():
        if v == value:
            return k
    return None


def get_exif_data(image: Image):
    meta = {}
    exif = image._getexif()

    interesting_tags = ["Make", "Model", "DateTime", "DateTimeOriginal", ]

    for tag in interesting_tags:
        index = key_of(EXIF_TAGS, tag)
        if index in exif.keys():
            meta[tag] = exif[index]
    return meta


def main():
    initialise()
    images = get_image_list()
    out = dict()
    for image in images:
        image_meta_data = process(image)
        out[image] = image_meta_data
    pp(out)
