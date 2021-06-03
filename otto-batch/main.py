#!/usr/bin/env python3

def initialise():
    pass


def get_image_list():
    pass


def get_exif_data(image):
    pass


def main():
    initialise()
    images = get_image_list()
    for image in images:
        image_meta_data = get_exif_data(image)
