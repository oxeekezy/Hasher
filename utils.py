from PIL import Image


def hash_image_generator(width: int, height: int, pixel_str: str):
    size: tuple = [width, height]
    img = Image.new(size=size, mode="RGB")

    pixel = 0
    for w in range(size[0]):
        for h in range(size[1]):
            img.putpixel((w, h), ((int(pixel_str[pixel]) * 255), 0, 0))
            pixel += 1

    return img
