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

# add gausion blur effect
def apply_gaussian_blur(image, radius):
    """
    Applies a Gaussian blur filter to the provided image.

    Args:
        image: The input image object.
        radius: The radius of the Gaussian blur filter (higher = more blur).

    Returns:
        Image: The image object with Gaussian blur applied.
    """

    blurred_image = image.filter(image_filter.GaussianBlur(radius=radius))
    return blurred_image

# add noise reduction effect
# def apply_noise_reduction(image):
#      """
#     Apply noise reduction of the provided image (may not work for all images).

#     Args:
#     - image: The input image object.

#     Returns:
#     - Image: The image object with noise reduction applied.
#     """
#     width, height = image.size
#     noise_reduced_image = Image.new('RGB', (width, height))

#     for x in range(1, width - 1):
#         for y in range(1, height - 1):
#             pixels = [
#             image.getpixel((x - 1, y)), image.getpixel((x + 1, y)),
#             image.getpixel((x, y - 1)), image.getpixel((x, y + 1))
#             ]
#             average_pixel = tuple(map(lambda p: sum(p) // 4, zip(*pixels)))
#             noise_reduced_image.putpixel((x, y), average_pixel)
        
#         return noise_reduced_image

# add sharpness effect
