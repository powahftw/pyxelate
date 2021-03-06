from PIL import Image, ImageDraw
import argparse


# MAIN FUNCTIONS
def create_pixelate(img, nsize):
    w, h = img.size

    imgpixel = img.copy()
    draw = ImageDraw.Draw(imgpixel)

    for i in range(h / nsize):
        for e in range(w / nsize):
            tempimg = img.crop((e * nsize, i * nsize, (e + 1) * nsize, (i + 1) * nsize))
            mfp = frequent_color(tempimg)  # GET THE MOST FREQUENT COLOR FOR A CERTAIN BLOCK
            draw.rectangle((e * nsize, i * nsize, (e + 1) * nsize, (i + 1) * nsize),
                           fill=mfp)  # SUBSTITUTE THE BLOCK WITH THE FREQUENCY COLOR

    return imgpixel


def frequent_color(img):  # THANKS TO http://blog.zeevgilovitz.com/detecting-dominant-colours-in-python/
    w, h = img.size
    pixels = img.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for cont, colour in pixels:
        if cont > most_frequent_pixel[0]:
            most_frequent_pixel = (cont, colour)

    return most_frequent_pixel[1]


# UTILITY
def fix_img_dim(img, w, h):
    half_new_w = (w / 10) * 10 / 2  # ROUNDING SIZE
    half_new_h = (h / 10) * 10 / 2

    crop_w1 = w / 2 - half_new_w
    crop_w2 = w / 2 + half_new_w
    crop_h1 = h / 2 - half_new_h
    crop_h2 = h / 2 + half_new_h

    new_img = img.crop((crop_w1, crop_h1, crop_w2, crop_h2))
    if (w * h) < 1500000:  # IF THE IMAGE IS REALLY SMALL WE GET BETTER RESULT BY MAKING IT LARGER FIRST
        print("NEW DIMENSION RESCALED - W: %d H: %d" % (half_new_h * 4, half_new_w * 4))
        return new_img.resize((half_new_w * 4, half_new_h * 4), Image.NEAREST)
    else:
        print("NEW DIMENSION - W: %d H: %d" % (half_new_w * 2, half_new_h * 2))
        return new_img


# MAIN
def main():
    p = argparse.ArgumentParser(description="Make an image a low-res version of it")
    p.add_argument("image", help="Image File Path")
    p.add_argument("-d", "-dimension", type=int, default=15, help="Size of PixelBlock")
    args = p.parse_args()

    print("\nWork in Progress... \n")

    try:
        img = Image.open(args.image)
    except IOError:
        print("Error: File does not appear to exist.")
        return 0

    w, h = img.size

    print("ORIGINAL DIMENSION - W: %d H: %d" % (w, h))
    new_img = fix_img_dim(img, w, h)

    img = create_pixelate(new_img, args.d)

    img.save('image_pixelate.jpg')
    print("We should be done :)")

    return 0


if __name__ == '__main__':
    main()
