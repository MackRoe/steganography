# python
from PIL import Image


def decode_image(file_location):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]
    rgb_rc = red_channel.convert('RGB')

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    # TODO: Fill in decoding functionality
    # -----------------------------------
    # loop through all pixels in encoded_image
    for x in range(x_size):
        print(x)
        for y in range(y_size):
            print(y)
            # xy = int(str(x) + str(y))
            # print('xy', xy)
            r,g,b = rgb_rc.getpixel((x, y))  # #ERROR!
            print('RGB', r,g,b)
            print('r', r)
            # check LSB
            binary_r = bin(r)
            length_binary = len(str(r))
            print(length_binary)
            if binary_r[length_binary-1] == 1:
                r,g,b = 255, 255, 255
            # check LSB
            elif binary_r[length_binary-1] == 0:
                r,g,b = 0, 0, 0
            decoded_image.putpixel((x,y), r,g,b)


    decoded_image.save("decoded_image.png")

print(decode_image("encoded_sample.png"))
