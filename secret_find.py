# python
from PIL import Image, ImageFont, ImageDraw


def decode_image(file_location):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]
    # rgb_rc = red_channel.convert('RGB')

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    # TODO: Fill in decoding functionality
    # -----------------------------------
    # loop through all pixels in encoded_image
    for x in range(x_size):
        # print(x)
        for y in range(y_size):
            # print(y)
            # xy = int(str(x) + str(y))
            # print('xy', xy)
            # r,g,b = rgb_rc.getpixel((x, y))
            # print('RGB', r,g,b)
            # print('r', r)
            # check LSB
            binary_r = bin(red_channel.getpixel((x, y)))
            # length_binary = len(str(r))
            # print(length_binary)

            # check if lsb of red_channel is 1
            if binary_r[-1] == '0':
                # make pixel black if LSB is 0
                pixels[x, y] = (255, 255, 255)
            else:
                # make pixel white
                pixels[x, y] = (0, 0, 0)

            # decoded_image.putpixel((x,y), (r,g,b))


    decoded_image.save("decoded_image4.png")

print(decode_image("encoded_sample.png"))
