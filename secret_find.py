# python
from PIL import Image


def decode_image(file_location):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    # TODO: Fill in decoding functionality
    # -----------------------------------
    # loop through all pixels in encoded_image
    for x in range(x_size):
        for y in range(y_size):
            r,g,b = red_channel.getpixel((xy))
            if bin.r[len(r)-1] == 1:
                r,g,b = 255, 255, 255
            elif bin.r[len(r)-1] == 0:
                r,g,b = 0, 0, 0
            decoded_image.putpixel(xy, r,g,b)
    # change LSB

    decoded_image.save("images/decoded_image.png")

decode_image("encoded_sample.png")
