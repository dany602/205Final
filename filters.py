# functions.py
# Author: Drake Goldsmith, Jasmin Medrano, Daniel Bonilla Urtis
# Class: CST 205
# Date: 05/13/24
# Brief Description: Contains image manipulation and search functions.

from PIL import Image


def apply_sepia(image):
    """
    Apply sepia filter to the provided image.

    Args:
    - image: The input image object.

    Returns:
    - Image: The image object with sepia filter applied.
    """
    def apply_sepia_pixel(p):
        # Tint shadows
        if p[0] < 63:
            r, g, b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)
        # Tint midtones
        elif p[0] > 62 and p[0] < 192:
            r, g, b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)
        # Tint highlights
        else:
            r = int(p[0] * 1.08)
            g, b = p[1], int(p[2] * 0.5)
        return r, g, b

    width, height = image.size
    sepia_image = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            sepia_pixel = apply_sepia_pixel(pixel)
            sepia_image.putpixel((x, y), sepia_pixel)

    return sepia_image

def apply_negative(image):
    """
    Apply negative filter to the provided image.

    Args:
    - image: The input image object.

    Returns:
    - Image: The image object with negative filter applied.
    """

    width, height = image.size
    negative_image = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            negative_pixel = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
            negative_image.putpixel((x, y), negative_pixel)

    return negative_image

def apply_grayscale(image):
    """
    Apply grayscale filter to the provided image.

    Args:
    - image: The input image object.

    Returns:
    - Image: The image object with grayscale filter applied.
    """

    width, height = image.size
    grayscale_image = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            grayscale_value = sum(pixel) // 3
            grayscale_pixel = (grayscale_value, grayscale_value, grayscale_value)
            grayscale_image.putpixel((x, y), grayscale_pixel)

    return grayscale_image

def create_thumbnail(image):
    """
    Create a thumbnail of the provided image (half the width and height).

    Args:
    - image: The input image object.

    Returns:
    - Image: The thumbnail image object.
    """

    width, height = image.size
    thumbnail = Image.new('RGB', (width // 2, height // 2))

    for x in range(0, width - 1, 2):
        for y in range(0, height - 1, 2):
            pixel = image.getpixel((x, y))
            thumbnail.putpixel((x // 2, y // 2), pixel)

    return thumbnail